var vm = new Vue({
    el: '#app',
    data: {
        host: host,
        sending_flag: false,
        sending_sms: false,
        sms_code_tip: '获取验证码',
        error_mobile: false,
        error_password: false,
        error_check_password: false,
        error_sms_code: false,
        error_mobile_message: '',
        error_sms_code_message: '',
        mobile: '',
        password: '',
        password2: '',
        sms_code: ''
    },
    methods: {
        // 检查手机号
        check_mobile: function (){
            var re = /^1[345789]\d{9}$/;
            if(re.test(this.mobile)) {
                this.error_mobile = false;
            } else {
                this.error_mobile_message = '您输入的手机号格式不正确';
                this.error_mobile = true;
                this.sending_sms = true;
            }
            if (this.error_mobile == false) {
                axios.get(this.host + '/mobiles/'+ this.mobile + '/count/', {
                    responseType: 'json'
                })
                    .then(response => {
                        if (response.data.count != 1) {
                            this.error_mobile_message = '手机号不存在';
                            this.error_mobile = true;
                            this.sending_sms = false;
                        } else {
                            this.error_mobile = false;
                            this.sending_sms = true;
                        }
                    })
                    .catch(error => {
                        console.log(error.response.data);
                        this.error_mobile = true;
                        this.sending_sms = false;
                        this.sending_flag = false;

                    })
            }
        },
        check_pwd: function (){
            var len = this.password.length;
            if(len<6||len>20){
                this.error_password = true;
            } else {
                this.error_password = false;
            }
        },
        check_cpwd: function (){
            if(this.password!=this.password2) {
                this.error_check_password = true;
            } else {
                this.error_check_password = false;
            }
        },
        check_sms_code: function(){
            if(!this.sms_code){
                this.error_sms_code_message = '请填写短信验证码';
                this.error_sms_code = true;
            } else {
                this.error_sms_code = false;
            }
        },
        // 发送手机短信验证码
        send_sms_code: function(){
            // 校验参数，保证输入框有数据填写
            if (this.sending_flag == true) {
                return;
            }
            if (this.sending_sms == false) {
                return;
            }
            this.check_mobile();
            if (this.error_mobile == true) {
                this.sending_flag = false;
                return;
            }
            this.sending_flag = true;
            // 向后端接口发送请求，让后端发送短信验证码
            axios.get(this.host + '/sms_codes/' + this.mobile + '/', {
                responseType: 'json'
            })
                .then(response => {
                    // 表示后端发送短信成功
                    // 倒计时60秒，60秒后允许用户再次点击发送短信验证码的按钮
                    var num = 60;
                    // 设置一个计时器
                    var t = setInterval(() => {
                        if (num == 1) {
                            // 如果计时器到最后, 清除计时器对象
                            clearInterval(t);
                            // 将点击获取验证码的按钮展示的文本回复成原始文本
                            this.sms_code_tip = '获取验证码';
                            // 将点击按钮的onclick事件函数恢复回去
                            this.sending_flag = false;
                        } else {
                            num -= 1;
                            // 展示倒计时信息
                            this.sms_code_tip = num + '秒';
                        }
                    }, 1000, 60)
                })
                .catch(error => {
                    if (error.response.status == 400) {
                        this.sms_code_tip = '发送异常';
                    } else {
                        console.log(error.response.data);
                    }
                    this.sending_flag = false;
                })
        },
        getCookie(name) {
            var value = ';' + document.cookie;
            var parts = value.split(';'+name+'=');
            if (parts.length === 2) return parts.pop().split(';').shift()
        },
        // 注册
        on_submit: function(){
            this.check_mobile();
            this.check_pwd();
            this.check_cpwd();
            this.check_sms_code();
            if(this.error_mobile == false && this.error_password == false && this.error_check_password == false && this.error_sms_code == false) {
                axios.put(this.host + '/users/forget/', {
                    password: this.password,
                    password2: this.password2,
                    mobile: this.mobile,
                    sms_code: this.sms_code
                },{
                    headers:{'X-CSRFToken': this.getCookie('csrftoken')}
                }, {
                    responseType: 'json',
                    withCredentials: true
                })
                    .then(response => {
                        // 记录用户的登录状态
                        sessionStorage.clear();
                        localStorage.clear();
                        // localStorage.token = response.data.token;
                        // localStorage.username = response.data.username;
                        // localStorage.user_id = response.data.id;
                        location.href = '/login.html';
                    })
                    .catch(error=> {
                        if (error.response.status == 400) {
                            if ('non_field_errors' in error.response.data) {
                                this.error_sms_code_message = error.response.data.non_field_errors[0];
                            } else {
                                this.error_sms_code_message = '验证码错误';
                            }
                            this.error_sms_code = true;
                        } else {
                            console.log(error.response.data);
                        }
                    })
            }
        }
    }
});