import request from '@/utils/request'

export function getGoodsList() {
  return request({
    url: '/show_goods',
    method: 'get'
  })
}

export function getGoodsOrderSales() {
  return request({
    url: '/statistics',
    method: 'get'
  })
}

export function delGoods(goods_id) {
  return request({
    url: `/del_goods/${goods_id}`,
    method: 'get',
  })
}

export function editGoods(data) {
  return request({
    url: '/modify_goods',
    method: 'post',
    data
  })
}

export function addGoods(data) {
  return request({
    url: '/add_goods',
    method: 'post',
    data
  })
}





