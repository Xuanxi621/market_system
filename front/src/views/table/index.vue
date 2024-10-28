<template>
  <div class="app-container">
    <el-dialog :title="d_title" :visible.sync="add_dialogVisible" width="30%" :before-close="handleClose">
      <el-form ref="form" :model="add_form" label-width="80px">
        <el-form-item label="食品名称">
          <el-input v-model="add_form.goods_name"></el-input>
        </el-form-item>
        <el-form-item label="价格">
          <el-input v-model="add_form.price"></el-input>
        </el-form-item>
        <el-form-item label="销售量">
          <el-input v-model="add_form.sales"></el-input>
        </el-form-item>
        <el-form-item label="生产日期">
          <el-date-picker v-model="add_form.manufacture_date" type="datetime" placeholder="选择日期" />
        </el-form-item>
        <el-form-item label="截止日期">
          <el-date-picker v-model="add_form.expiration_date" type="datetime" placeholder="选择日期" />
        </el-form-item>
        <el-form-item style="margin-top: 80px;margin-left: 20px;">
          <el-button type="primary" @click="addSubmit">确定</el-button>
          <el-button @click="add_dialogVisible = false">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <el-dialog :title="d_title" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="食品名称">
          <el-input v-model="form.goods_name" disabled></el-input>
        </el-form-item>
        <el-form-item label="价格">
          <el-input v-model="form.price"></el-input>
        </el-form-item>
        <el-form-item label="销售量">
          <el-input v-model="form.sales"></el-input>
        </el-form-item>
        <el-form-item label="生产日期">
          <el-date-picker v-model="form.manufacture_date" type="datetime" placeholder="选择日期" />
        </el-form-item>
        <el-form-item label="截止日期">
          <el-date-picker v-model="form.expiration_date" type="datetime" placeholder="选择日期" />
        </el-form-item>
        <el-form-item style="margin-top: 80px;margin-left: 20px;">
          <el-button type="primary" @click="onSubmit">确定</el-button>
          <el-button @click="dialogVisible = false">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <el-button type="success" @click="handleAdd" style="float: left;">添加食品</el-button>
    <el-button type="primary" @click="selectGoodsOrderSales" style="float: left;margin-right: 50px;">销量排序</el-button>

    <el-table v-loading="listLoading" :data="list" element-loading-text="加载中" border fit highlight-current-row
      max-height="550">
      <el-table-column align="center" label="ID" width="100">
        <template v-slot="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="商品名" width="150" align="center">
        <template v-slot="scope">
          {{ scope.row.goods_name }}
        </template>
      </el-table-column>
      <el-table-column label="价格" width="100" align="center">
        <template v-slot="scope">
          <span>{{ scope.row.price }}</span>
        </template>
      </el-table-column>
      <el-table-column label="销售量" width="150" align="center">
        <template v-slot="scope">
          {{ scope.row.sales }}
        </template>
      </el-table-column>
      <el-table-column label="生产日期" width="200" align="center">
        <template v-slot="scope">
          {{ formatDate(scope.row.manufacture_date) }}
        </template>
      </el-table-column>
      <el-table-column label="过期日期" width="200" align="center">
        <template v-slot="scope">
          {{ formatDate(scope.row.expiration_date) }}
        </template>
      </el-table-column>
      <el-table-column label="操作" width="300%" align="center">
        <template v-slot="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getGoodsList, getGoodsOrderSales, delGoods, editGoods, addGoods } from '@/api/table'

export default {
  data() {
    return {
      list: null,
      listLoading: true,
      dialogVisible: false,
      add_dialogVisible: false,
      form: this.initForm(),
      add_form: this.initForm(),
      d_title: '食品添加'
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    initForm() {
      return {
        good_id: '',
        goods_name: '',
        price: '',
        sales: '',
        manufacture_date: '',
        expiration_date: ''
      }
    },
    fetchData() {
      this.listLoading = true
      getGoodsList().then(response => {
        this.list = response
        this.listLoading = false
      })
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(() => {
          done()
        })
        .catch(() => { })
    },
    validateForm(form) {
      const fields = ['goods_name', 'price', 'sales', 'manufacture_date', 'expiration_date']
      for (const field of fields) {
        if (!form[field]) {
          this.$message.error(`${field}不能为空`)
          return false
        }
      }
      return true
    },
    addSubmit() {
      if (this.validateForm(this.add_form)) {
        addGoods(this.add_form).then(res => {
          if (res === 200) {
            this.$message.success('添加成功')
            this.add_dialogVisible = false
            this.add_form = this.initForm()
            this.fetchData()
          }
        })
      }
    },
    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return date.toISOString().split('T')[0]; // 返回 YYYY-MM-DD 格式
    },
    onSubmit() {
      if (this.validateForm(this.form)) {
        editGoods(this.form).then(res => {
          if (res === 200) {
            this.$message.success('编辑成功')
            this.dialogVisible = false
            this.form = this.initForm()
            this.fetchData()
            this.d_title = "食品添加"
          }
        })
      }
    },
    handleEdit(idx, val) {
      this.d_title = "食品编辑"
      this.dialogVisible = true
      this.form = val
    },
    handleAdd() {
      this.d_title = "食品添加"
      this.add_dialogVisible = true
    },
    selectGoodsOrderSales() {
      getGoodsOrderSales().then(response => {
        this.list = response
      })
    },
    handleDelete(val) {
      delGoods(val.good_id).then(() => {
        this.$message.success('删除成功')
        this.fetchData()
      })
    }
  }
}
</script>
