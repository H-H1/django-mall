var vm = new Vue({
    el: '#apps',
    data: {
        host,
        user_id: sessionStorage.user_id || localStorage.user_id,
        token: sessionStorage.token || localStorage.token,
        username: '',
        mobile: '',
        content: '',
        type: 'mobile',
        feed_error: false,
        feed_error_message: ''
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
                    this.mobile = response.data.mobile;
                })
                .catch(error => {
                    if (error.response.status==401 || error.response.status==403) {
                        location.href = '/login.html?next=/wap/member/member.html';
                    }
                });
        } else {
            location.href = '/login.html?next=/wap/member/member_feedback.html';
        }
    },
    methods: {
        check_content: function (){
            var len = this.content.length;
            if(len<10||len>255) {
                this.feed_error = true;
                this.feed_error_message = '输入字数不符合';
                return;

            } else {
                this.feed_error = false;
            }
        },
        // 保存反馈
        save_feedback: function(){
            this.check_content();
            if (this.feed_error == true) {
                return;
            }
            axios.post(this.host + '/feedback/', {
                type: this.type,
                content: this.content,
                // user_id:this.user_id,
                // username:this.username
                },
                {
                    headers: {
                        'Authorization': 'JWT ' + this.token
                    },
                    responseType: 'json'
                })
                .then(response => {
                    this.feed_error = true;
                    this.feed_error_message = '提交成功'
                    window.setTimeout("window.location='/wap/member/member.html'",1000);
                })
                .catch(error => {
                    alert(error.data);
                });
        }
    }
});