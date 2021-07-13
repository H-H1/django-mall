var vm = new Vue({
    el: '#applist',
    delimiters: ['[[', ']]'], // 修改vue模板符号，防止与django冲突
    data: {
        host: host,
        username: sessionStorage.username || localStorage.username,
        user_id: sessionStorage.user_id || localStorage.user_id,
        token: sessionStorage.token || localStorage.token,
        page: 1, // 当前页数
        page_size: 6, // 每页数量
        count: 0,  // 总数量
        skus: [], // 数据
        query: '',  // 查询关键字
        show_list: true,
    },
    mounted: function(){
        this.query = this.get_query_string('q');
        this.get_search_result();
        // this.get_cart();
    },
    methods: {
        logout(){
            sessionStorage.clear();
            localStorage.clear();
            location.href = '/login.html';
        },
        // 获取url路径参数
        get_query_string: function(name){
            var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
            var r = window.location.search.substr(1).match(reg);
            if (r != null) {
                return decodeURI(r[2]);
            }
            return null;
        },
        // 请求查询结果
        get_search_result: function(){
            axios.get(this.host+'/skus/search/', {
                    params: {
                        text: this.query,
                        //page: this.page,
                        //page_size: this.page_size,
                    },
                    responseType: 'json'
                })
                .then(response => {
                    // this.count = response.data.count;
                    this.skus = response.data.results;
                    for(var i=0; i<this.skus.length; i++){
                        this.skus[i].url = '/wap/shop/goods/' + this.skus[i].id + ".html";
                    }
                })
                .catch(error => {
                    console.log(error.response.data);
                })
        },
        on_list:function(){
            if (this.show_list===true){
                this.show_list = false;
            }else{
                this.show_list = true;
            }
        },
        search:function(){
            location.href = '/wap/shop/search.html';
        },
    }
});