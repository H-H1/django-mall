var vm = new Vue({
    el: '#app',
    data: {
        host,
        user_id: sessionStorage.user_id || localStorage.user_id,
        token: sessionStorage.token || localStorage.token,
		avatar: sessionStorage.avatar || localStorage.avatar,
        username: '',
        mobile: '',
        email: '',
        email_active: false,
        set_email: false,
        send_email_btn_disabled: false,
        send_email_tip: '重新发送验证邮件',
        email_error: false,
        histories: [],
        password: '',
        passwordn1: '',
        password2: '',
        error_pwd_message: '',
        error_password:false,
        error_newpwd_message: '',
        error_newpwd:false,

    },
    mounted: function(){
        // 判断用户的登录状态
        if (this.user_id && this.token) {
            axios.get(this.host + '/user/', {
                // 向后端传递JWT token的方法
                headers: {
                    'Authorization': 'JWT ' + this.token
                },
                responseType: 'json',
            })
                .then(response => {
                    // 加载用户数据
                    this.user_id = response.data.id;
                    this.username = response.data.username;
					//this.avatar = response.data.avatar;
                    this.mobile = response.data.mobile;
                    this.email = response.data.email;
                    this.email_active = response.data.email_active;
                })
                .catch(error => {
                    if (error.response.status==401 || error.response.status==403) {
                        location.href = '/login.html?next=/wap/member/member.html';
                    }
                });
        } else {
            location.href = '/login.html?next=/wap/member/member.html';
        }
    },
    methods: {
        // 退出
        logout: function(){
            sessionStorage.clear();
            localStorage.clear();
            location.href = '/login.html';
        },
        // 保存email
        save_email: function(){
            var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
            if(re.test(this.email)) {
                this.email_error = false;
            } else {
                this.email_error = true;
                return;
            }
            axios.put(this.host + '/email/',
                { email: this.email },
                {
                    headers: {
                        'Authorization': 'JWT ' + this.token
                    },
                    responseType: 'json'
                })
                .then(response => {
                    this.set_email = false;
                    this.send_email_btn_disabled = true;
                    this.send_email_tip = '已发送验证邮件'
                })
                .catch(error => {
                    alert(error.data);
                });
        },
        // 检查旧密码
        check_pwd: function (){
            var len = this.password.length;
            if(len<6||len>20){
                this.error_password = true;
                this.error_pwd_message = "密码不能小于6位"
            } else {
                this.error_password = false;
            }
        },
        // 检查新密码
        check_pwd1: function (){
            var len = this.passwordn1.length;
            if(len<6||len>20){
                this.error_password = true;
                this.error_pwd_message = "密码不能小于6位"
            } else {
                this.error_password = false;
            }
        },
        check_pwd2 : function (){
            if(this.passwordn1!=this.password2) {
                this.error_newpwd = true;
                this.error_newpwd_message = "两次输入的新密码不一致";
            } else {
                this.error_newpwd = false;
            }
        },
        on_submit: function(){
            this.check_pwd();
            this.check_pwd1();
            this.check_pwd2();

            if(this.error_password == false && this.error_newpwd == false) {
                axios.put(this.host + '/users/pwd/', {
                    password: this.password,
                    password2: this.password2,
                },
                    {
                    headers:{
                        'Authorization': 'JWT ' + this.token
                    },
                    responseType: 'json',
                    withCredentials: true
                },
                    {
                    responseType: 'json'
                })
                    .then(response => {
                  		//alert("修改密码成功");
                        //location.href = '/wap/member/member.html';
                  		this.error_newpwd_message = '修改密码成功';
                  		this.error_newpwd = true;
                  		window.setTimeout("window.location='/wap/member/member.html'",2000); 
                    })
                    .catch(error=> {
                        if (error.response.status == 400) {
                            if ('non_field_errors' in error.response.data) {
                                this.error_newpwd_message = error.response.data.non_field_errors;
                            } else {
                                this.error_newpwd_message = '修改出错';
                            };
							this.error_newpwd = true;
                        } else {
                            console.log(error.response.data);
                        }
                    })
            }
        },
    }
});