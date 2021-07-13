var vm = new Vue({
    el: '#applist',
    delimiters: ['[[', ']]'], // 修改vue模板符号，防止与django冲突
    data: {
        host: host,
        username: sessionStorage.username || localStorage.username,
        user_id: sessionStorage.user_id || localStorage.user_id,
        token: sessionStorage.token || localStorage.token,
        id: '', // 当前商品类别
        brand: '', //品牌ID
        page: 1, // 当前页数
        page_size: 8, // 每页数量
        ordering: '-create_time', // 排序
        count: 0,  // 总数量
        skus: [], // 数据
        pr_show: true,
        show_list: true,
    },
    computed: {
        total_page: function(){  // 总页数
            return Math.ceil(this.count/this.page_size);
        },
        next: function(){  // 下一页
            if (this.page >= this.total_page) {
                return 0;
            } else {
                return this.page + 1;
            }
        },
        previous: function(){  // 上一页
            if (this.page <= 0 ) {
                return 0;
            } else {
                return this.page - 1;
            }
        },
        page_nums: function(){  // 页码
            // 分页页数显示计算
            // 1.如果总页数<=5
            // 2.如果当前页是前3页
            // 3.如果当前页是后3页,
            // 4.既不是前3页，也不是后3页
            var nums = [];
            if (this.total_page <= 5) {
                for (var i=1; i<=this.total_page; i++){
                    nums.push(i);
                }
            } else if (this.page <= 3) {
                nums = [1, 2, 3, 4, 5];
            } else if (this.total_page - this.page <= 2) {
                for (var i=this.total_page; i>this.total_page-5; i--) {
                    nums.push(i);
                }
            } else {
                for (var i=this.page-2; i<this.page+3; i++){
                    nums.push(i);
                }
            }
            return nums;
        }
    },
    created: function(){
        var self = this;
        window.onscroll = function(){
            //变量scrollTop是滚动条滚动时，距离顶部的距离
            var scrollTop = document.documentElement.scrollTop||document.body.scrollTop;
            // console.log(scrollTop);
            //变量windowHeight是可视区的高度
            var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;
            // console.log(windowHeight);
            //变量scrollHeight是滚动条的总高度
            var scrollHeight = document.documentElement.scrollHeight||document.body.scrollHeight;
            // console.log(scrollHeight);
            //滚动条到底部的条件
            if(scrollTop+windowHeight==scrollHeight){
                //加载下一页
                console.log("距顶部"+scrollTop+"可视区高度"+windowHeight+"滚动条总高度"+scrollHeight);
                self.page += 1;
                console.log(self.page);
                console.log(self.count);
                if (self.page * 8 <= self.count){
                    self.get_skus();
                }
            }
        }
    },
    mounted: function(){
        this.id = this.get_query_string('id');
        this.brand = this.get_query_string('brand');
        this.get_skus();
    },
    methods: {
        logout(){
            sessionStorage.clear();
            localStorage.clear();
            location.href = '/login.html';
        },
        get_query_string: function(name){
            var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
            var r = window.location.search.substr(1).match(reg);
            if (r !== null) {
                return decodeURI(r[2]);
            }
            return null;
        },
        // 请求商品数据
        get_skus: function(){
            if (this.brand){
                console.log("加载品牌数据");
                axios.get(this.host+'/categories/brand/', {
                    params: {
                        brand: this.brand,
                        page: this.page,
                        page_size: this.page_size,
                        ordering: this.ordering
                    },
                    responseType: 'json'
                })
                    .then(response => {
                        this.count = response.data.count;
                        this.skus = response.data.results;
                        for(var i=0; i<this.skus.length; i++){
                            this.skus[i].url = '/wap/shop/goods/' + this.skus[i].id + ".html";
                        }
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    })
            }else{
                axios.get(this.host+'/categories/skus/', {
                    params: {
                        id: this.id,
                        page: this.page,
                        page_size: this.page_size,
                        ordering: this.ordering
                    },
                    responseType: 'json'
                })
                    .then(response => {
                        console.log(response.status);
                        this.count = response.data.count;
                        this.skus = this.skus.concat(response.data.results);
                        for(var i=0; i<this.skus.length; i++){
                            this.skus[i].url = '/wap/shop/goods/' + this.skus[i].id + ".html";
                        }
                    })
                    .catch(error => {
                        console.log(error.response.data);
                    })}
        },
        // 点击排序
        on_sort: function(ordering){
            if (ordering == "price"){
                this.skus = [];
                this.pr_show = false;
                this.page = 1;
                this.ordering = ordering;
                this.get_skus();
            }
            if (ordering == "-price"){
                this.skus = [];
                this.pr_show = true;
                this.page = 1;
                this.ordering = ordering;
                this.get_skus();
            }
            if (ordering != this.ordering) {
                this.skus = [];
                this.page = 1;
                this.ordering = ordering;
                this.get_skus();
            }
        },
        on_list:function(){
            if (this.show_list===true){
                this.show_list = false;
            }else{
                this.show_list = true;
            }
        },
    }
});