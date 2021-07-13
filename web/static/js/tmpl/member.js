$(function() {
    if (getQueryString('key') != '') {
        var a = getQueryString('key');
        var e = getQueryString('username');
        addCookie('key', a);
        addCookie('username', e)
    } else {
        var a = getCookie('key')
    }
    if (a) {
        $.ajax({
            type: 'post',
            url: ApiUrl + '/index.php?act=member_index',
            data: {
                key: a
            },
            dataType: 'json',
            success: function(a) {
                checkLogin(a.login);
                var e = '<div class="member-info" style="margin-top:-4.5rem">' + '<div class="user-avatar"> <img src="' + a.datas.member_info.avator + '"/> </div>' + '<div class="user-name"> <span>' + a.datas.member_info.user_name + "<sup>" + a.datas.member_info.level_name + "</sup></span> </div>" + '<div class="user-name"> <span style="font-weight:normal">ID：' + a.datas.member_info.user_id + "</span> </div>" + "</div>" + '<div class="member-team"><span><a href="../distributor/team.html"><em>' + a.datas.member_info.team_level + "</em>" + "<p>股东级别</p>" + '</a> </span><span class="team_right"><a href="../distributor/team_commission.html"><em>&yen;' + a.datas.member_info.team_commission + "</em>" + "<p>股东分红</p>" + '</a> </span></div>';
                $('.member-top').html(e);
                var e = '<li><a href="order_list.html?data-state=state_new">' + (a.datas.member_info.order_nopay_count > 0 ? "<em></em>": "") + '<i class="cc-01"></i><p>待付款</p></a></li>' + '<li><a href="order_list.html?data-state=state_send">' + (a.datas.member_info.order_noreceipt_count > 0 ? "<em></em>": "") + '<i class="cc-02"></i><p>待收货</p></a></li>' + '<li><a href="order_list.html?data-state=state_notakes">' + (a.datas.member_info.order_notakes_count > 0 ? "<em></em>": "") + '<i class="cc-03"></i><p>待自提</p></a></li>' + '<li><a href="order_list.html?data-state=state_noeval">' + (a.datas.member_info.order_noeval_count > 0 ? "<em></em>": "") + '<i class="cc-04"></i><p>待评价</p></a></li>' + '<li><a href="member_refund.html">' + (a.datas.member_info.
                return > 0 ? "<em></em>": "") + '<i class="cc-05"></i><p>退款/退货</p></a></li>';
                $('#order_ul').html(e);
                var e = '<li><a href="predepositlog_list.html"><i class="cc-06"></i><p>预存款</p></a></li>' + '<li><a href="rechargecardlog_list.html"><i class="cc-07"></i><p>充值卡</p></a></li>' + '<li><a href="voucher_list.html"><i class="cc-08"></i><p>代金券</p></a></li>' + '<li><a href="/wap/tmpl/member/pd_chongzhi.html"><i class="cc-09"></i><p>充值</p></a></li>'+ '<li><a href="points_fanyong_list.html?data-state=state_new"><i class="cc-09"></i><p>全返明细</p></a></li>';
                $("#asset_ul").html(e);
				
				if(a.datas.member_info.distributor_level){
					$('#distributor_level').html(a.datas.member_info.distributor_level);
				}
				var e = '<li><a href="/shop/distributor/dis_term.html"><i class="cc-12"></i><p>团队管理</p></a></li>' + '<li><a href="/shop/distributor/dis_spread.html"><i class="cc-13"></i><p>推广二维码</p></a></li>' + '<li><a href="../distributor/dis_record.html"><i class="cc-14"></i><p>分销记录</p></a></li>' + '<li><a href="../distributor/dis_commission.html"><i class="cc-15"></i><p>佣金明细</p></a></li>' + '<li><a href="../shop/distributor/withdraw.html"><i class="cc-16"></i><p>提现</p></a></li>';
				$('#distributor_ul').html(e);
				
				if(a.datas.public_area.length>0){
					var e = '';
					for(var ii=0;ii<a.datas.public_area.length;ii++){
						var area_info = a.datas.public_area[ii];
						e += '<dl class="mt5"><dt><h3><i class="mc-06"></i>'+area_info.item_name+'</h3></dt><dd><ul><li><a href="../distributor/public_position.html?area_id='+area_info.item_id+'"><i class="cc-17"></i><p>我的卡位</p></a></li>' + '<li><a href="../distributor/public_term.html?area_id='+area_info.item_id+'"><i class="cc-18"></i><p>下级人员</p></a></li>' + '<li><a href="../distributor/public_commission.html?area_id='+area_info.item_id+'"><i class="cc-19"></i><p>红包明细</p></a></li></ul></dd></dl>';
					}
					$('#public_areas').html(e);
				}else{
					$('#public_areas').hide();
				}
				
                return false
            }
        })
    } else {
        var i = '<div class="member-info">' + '<a href="login.html" class="default-avatar" style="display:block;"></a>' + '<a href="/login.html" class="to-login">点击登录</a>' + "</div>" + '<div class="member-collect"><span><a href="/login.html"><i class="favorite-goods"></i>' + "<p>商品收藏</p>" + '</a> </span><span><a href="/login.html"><i class="favorite-store"></i>' + "<p>店铺收藏</p>" + '</a> </span><span><a href="login.html"><i class="goods-browse"></i>' + "<p>我的足迹</p>" + "</a> </span></div>";
        $(".member-top").html(i);
        var i = '<li><a href="login.html"><i class="cc-01"></i><p>待付款</p></a></li>' + '<li><a href="login.html"><i class="cc-02"></i><p>待收货</p></a></li>' + '<li><a href="login.html"><i class="cc-03"></i><p>待自提</p></a></li>' + '<li><a href="login.html"><i class="cc-04"></i><p>待评价</p></a></li>' + '<li><a href="login.html"><i class="cc-05"></i><p>退款/退货</p></a></li>';
        $('#order_ul').html(i);
        var i = '<li><a href="predepositlog_list.html"><i class="cc-06"></i><p>余额</p></a></li>' + '<li><a href="rechargecardlog_list.html"><i class="cc-07"></i><p>充值卡</p></a></li>' + '<li><a href="voucher_list.html"><i class="cc-08"></i><p>代金券</p></a></li>' + '<li style="display:none;"><a href="redpacket_list.html"><i class="cc-09"></i><p>红包</p></a></li>';
        $('#asset_ul').html(i);
        return false
    }
    $.scrollTransparent()
});