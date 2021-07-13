var vm = new Vue({
    el: '#app',
    data: {
        host: host,
        user_id: sessionStorage.user_id || localStorage.user_id,
        token: sessionStorage.token || localStorage.token,
        username: sessionStorage.username || localStorage.username,
        is_show_edit: false,
        is_show_view: true,
        provinces: [],
        cities: [],
        districts: [],
        addresses: [],
        limit: '',
        default_address_id: '',
        form_address: {
            receiver: '',
            province_id: '',
            city_id: '',
            district_id: '',
            place: '',
            mobile: '',
            email: '',
        },
        error_receiver: false,
        error_place: false,
        error_mobile: false,
        error_email: false,
        editing_address_index: '', // 正在编辑的地址在addresses中的下标，''表示新增地址
    },
    mounted: function(){
        axios.get(this.host + '/areas/', {
            responseType: 'json'
        })
            .then(response => {
                this.provinces = response.data;
            })
            .catch(error => {
                alert(error.response.data);
            });
        // 补充获取地址数据的请求
        axios.get(this.host + '/addresses/', {
            headers: {
                'Authorization': 'JWT ' + this.token
            },
            responseType: 'json'
        })
            .then(response => {
                this.addresses = response.data.addresses;
                this.limit = response.data.limit;
                this.default_address_id = response.data.default_address_id;
            })
            .catch(error => {
                status = error.response.status;
                if (status == 401 || status == 403) {
                    location.href = 'login.html?next=/wap/member/member.html';
                } else {
                    alert(error.response.data.detail);
                }
            })
    },
    watch: {
        'form_address.province_id': function(){
            if (this.form_address.province_id) {
                axios.get(this.host + '/areas/'+ this.form_address.province_id + '/', {
                    responseType: 'json'
                })
                    .then(response => {
                        this.cities = response.data.subs;
                    })
                    .catch(error => {
                        console.log(error.response.data);
                        this.cities = [];
                    });
            }
        },
        'form_address.city_id': function(){
            if (this.form_address.city_id){
                axios.get(this.host + '/areas/'+ this.form_address.city_id + '/', {
                    responseType: 'json'
                })
                    .then(response => {
                        this.districts = response.data.subs;
                    })
                    .catch(error => {
                        console.log(error.response.data);
                        this.districts = [];
                    });
            }
        }
    },
    methods: {
        // 退出
        logout: function(){
            sessionStorage.clear();
            localStorage.clear();
            location.href = '/login.html';
        },
        clear_all_errors: function(){
            this.error_receiver = false;
            this.error_mobile = false;
            this.error_place = false;
            this.error_email = false;
        },
        // 展示新增地址界面
        show_add: function(){
            this.clear_all_errors();
            this.editing_address_index = '';
            this.form_address.receiver = '';
            this.form_address.province_id = '';
            this.form_address.city_id = '';
            this.form_address.district_id = '';
            this.form_address.place = '';
            this.form_address.mobile = '';
            // this.form_address.tel = '';
            this.form_address.email = '';
            this.is_show_edit = true;
            this.is_show_view = false;
        },
        // 展示编辑地址界面
        show_edit: function(index){
            this.clear_all_errors();
            this.editing_address_index = index;
            // 只获取数据，防止修改form_address影响到addresses数据
            this.form_address = JSON.parse(JSON.stringify(this.addresses[index]));
            this.is_show_edit = true;
            this.is_show_view = false;
        },
        check_receiver: function(){
            if (!this.form_address.receiver) {
                this.error_receiver = true;
            } else {
                this.error_receiver = false;
            }
        },
        check_place: function(){
            if (!this.form_address.place) {
                this.error_place = true;
            } else {
                this.error_place = false;
            }
        },
        check_mobile: function(){
            var re = /^1[345789]\d{9}$/;
            if(re.test(this.form_address.mobile)) {
                this.error_mobile = false;
            } else {
                this.error_mobile = true;
            }
        },
        check_email: function(){
            if (this.form_address.email) {
                var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
                if(re.test(this.form_address.email)) {
                    this.error_email = false;
                } else {
                    this.error_email = true;
                }
            }
        },
        // 保存地址
        save_address: function(){
            if (this.error_receiver || this.error_place || this.error_mobile || this.error_email || !this.form_address.province_id || !this.form_address.city_id || !this.form_address.district_id ) {
                alert('信息填写有误！');
            } else {
                // this.form_address.title = this.form_address.receiver;
                if (this.editing_address_index === '') {
                    // 新增地址
                    axios.post(this.host + '/addresses/', this.form_address, {
                        headers: {
                            'Authorization': 'JWT ' + this.token
                        },
                        responseType: 'json'
                    })
                        .then(response => {
                            // 将新地址添加大数组头部
                            // this.addresses.splice(0, 0, response.data);
                            // this.is_show_edit = false;
                            // this.is_show_view = true;
                            location.href='/wap/member/address_list.html'
                        })
                        .catch(error => {
                            console.log(error.response.data);
                        })
                } else {
                    // 修改地址
                    axios.put(this.host + '/addresses/' + this.addresses[this.editing_address_index].id + '/', this.form_address, {
                        headers: {
                            'Authorization': 'JWT ' + this.token
                        },
                        responseType: 'json'
                    })
                        .then(response => {
                            this.addresses[this.editing_address_index] = response.data;
                            this.is_show_edit = false;
                            this.is_show_view = true;
                        })
                        .catch(error => {
                            alert(error.response.data.detail || error.response.data.message);
                        })
                }
            }
        },
        // 删除地址
        del_address: function(index){
            axios.delete(this.host + '/addresses/' + this.addresses[index].id + '/', {
                headers: {
                    'Authorization': 'JWT ' + this.token
                },
                responseType: 'json'
            })
                .then(response => {
                    // 从数组中移除地址
                    this.addresses.splice(index, 1);
                })
                .catch(error => {
                    console.log(error.response.data);
                })
        },
        // 设置默认地址
        set_default: function(index){
            axios.put(this.host + '/addresses/' + this.addresses[index].id + '/status/', {}, {
                headers: {
                    'Authorization': 'JWT ' + this.token
                },
                responseType: 'json'
            })
                .then(response => {
                    this.default_address_id = this.addresses[index].id;
                })
                .catch(error => {
                    console.log(error.response.data);
                })
        }
    }
})