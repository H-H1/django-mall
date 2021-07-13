var vm = new Vue({
    el: '#applist',
    data: {
        host,
        user_id: sessionStorage.user_id || localStorage.user_id,
        token: sessionStorage.token || localStorage.token,
        brands:[],
        categorys: [],
        category: [],
        isShow: true,
        pp_show: true,
        pl_show: false,
        sel:0,
    },
    mounted: function(){
        // 获取商品品牌数据
        this.brand();
        axios.get(this.host + '/categorys/', {
            responseType: 'json'
            })
            .then(response => {
                this.categorys = response.data.results;
            })
            .catch(error => {
                console.log(error.response.data);
            });

    },
    methods: {
        //
        showToggle:function(e){
            this.isShow = !this.isShow;
        },
        cgory:function (e) {
            console.log(e);
            this.pp_show = false;
            this.pl_show = true;
            this.sel = e;
            axios.get(this.host + '/category/' + e + '/', {
                responseType: 'json'
            })
                .then(response => {
                    this.category = response.data;
                })
                .catch(error => {
                    console.log(error.response.data);
                });
        },
        brand:function() {
            axios.get(this.host + '/brands/', {
                responseType: 'json'
                })
                .then(response => {
                    this.brands = response.data.results;
                    // this.brands = response.data;
                })
                .catch(error => {
                    console.log(error.response.data);
            });
            this.pp_show = true;
            this.pl_show = false;
            this.sel = 0;
        },
    }
});