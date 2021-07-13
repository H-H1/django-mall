var vm = new Vue({
    el: '#app',
    data: {
        host,
        username: sessionStorage.username || localStorage.username,
        user_id: sessionStorage.user_id || localStorage.user_id,
        token: sessionStorage.token || localStorage.token,
        sku_id: '',
        sku_count: 1,
        sku_price: 100,
        isShow: false,
        specShow: false,
        isNav: false,
        show_tran: true,
    },
    mounted: function(){
        this.get_sku_id();
        if (this.user_id) {
            axios.post(this.host+'/browse_histories/', {
                sku_id: this.sku_id
            }, {
                headers: {
                    'Authorization': 'JWT ' + this.token
                }
            })
        }
    },
    created: function(){
        var self = this;
        window.onscroll = function(){
            //变量scrollTop是滚动条滚动时，距离顶部的距离
            var scrollTop = document.documentElement.scrollTop||document.body.scrollTop;
            //滚动条到底部的条件
            if(scrollTop>=20){
                self.isNav = true;
                self.show_tran = false;
            }else{
                self.show_tran = true;
                self.isNav = false;
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
        // 从路径中提取sku_id
        get_sku_id: function(){
            var re = /^\/wap\/shop\/goods\/(\d+).html$/;
            this.sku_id = document.location.pathname.match(re)[1];
            console.log(this.sku_id);
        },
        // 减小数值
        on_minus: function(){
            if (this.sku_count > 1) {
                this.sku_count--;
            }
        },
        // 添加购物车
        add_cart: function(){
            axios.post(this.host+'/cart/', {
                sku_id: parseInt(this.sku_id),
                count: this.sku_count
            }, {
                headers: {
                    'Authorization': 'JWT ' + this.token
                },
                responseType: 'json',
                // 指明前端发送跨域请求的时候携带cookie
                withCredentials: true
            })
                .then(response => {
                    alert('添加购物车成功');
                    this.cart_total_count += response.data.count;
                    this.specShow = false;
                })
                .catch(error => {
                    if ('non_field_errors' in error.response.data) {
                        alert(error.response.data.non_field_errors[0]);
                        this.specShow = false;
                    } else {
                        alert('添加购物车失败');
                        this.specShow = false;
                    }
                    console.log(error.response.data);
                })
        },
        // 点击显示/隐藏
        showToggle: function(){
            this.isShow = !this.isShow;
        },
        showSpec: function(){
            this.specShow = !this.specShow;
        },
        goodsDetail: function () {
            console.log("goodsdetail");
        },
        goodsComment: function () {
            console.log("goodsComment");
        },
        goodsDesc: function () {
            console.log("goodsDesc");
        },
        // 获取购物车数据
        get_cart: function(){
        },
        // 获取热销商品数据
        get_hot_goods: function(){
        },
        // 获取商品评价信息
        get_comments: function(){
        },
    }
});