new Vue({
    delimiters: ['[[', ']]'],
    el:'#app_si01',
    data:{
        lists: [],
        listProvinces: [],
        listDistricts: [],
        errors: [],
        sector: 7,
        total: 0,
        cumple: 0,
        nocumple: 0,
        avan: 0,
        anio: 0,
        mes: 0,
    },
    created:function(){
        this.listYears();
    },
    methods:{
        listYears: function(){
            let fec = new Date();
            var selectYear = document.getElementById("anio");
            for(var i = 2024; i<=fec.getFullYear(); i++)selectYear.options.add(new Option(i,i));
            var selectMonth = document.getElementById("mes");
            for(var i = 1; i<=12; i++)selectMonth.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));
        },

        listDistritos(e) {
            axios.get('filterDist/', { params: { id: e.target.value } })
            .then(respuesta => {
                this.listDistricts = respuesta.data
            });
        },

        sendFormat: function (e) {
            var self = this
            var csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
            var formData = new FormData(e.target)

            if(this.anio == 0){
                this.anio = new Date().getFullYear();
                formData.set('anio', this.anio);
            }
            if(this.mes == 0){
                this.mes = new Date().getMonth()+1;
                formData.set('mes', this.mes);
            }

            var nameMonth = new Date(this.mes.toString()).toLocaleString('default', { month: 'long' });
            $('.nameMonthYear').text(nameMonth.toUpperCase()+' '+this.anio);

            axios({
                headers: { 'X-CSRFToken': csrfmiddlewaretoken, 'Content-Type': 'multipart/form-data' },
                method: 'POST',
                url: 'list/',
                data: formData
            }).then(response => {
                self.lists = response.data
                self.total = response.data[0].total
                self.cumple = response.data[0].cumple
                self.nocumple = response.data[0].total - response.data[0].cumple

                setTimeout(function() {
                    $('table').trigger('footable_redraw');
                    $('.chart').data('easyPieChart').update(response.data[0].avance);
                }, 100);
            }).catch(e => {
                this.errors.push(e)
            })
        },

        PrintExcel() {
            let prov = $("#provincia").val();
            let dist = $("#distrito").val();
            url_ = window.location.origin + window.location.pathname + 'print/?sector='+this.sector+'&prov='+prov+'&dist='+dist+'&anio='+this.anio+'&mes='+this.mes;
            window.open(url_, '_parent');
        },
    },
})