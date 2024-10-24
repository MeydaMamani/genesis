new Vue({
    delimiters: ['[[', ']]'],
    el:'#app_si0201',
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
        reportNom: true,
        tb_sano: true,
        tb_prematuro: false
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
                self.total = response.data[2].total
                self.cumple = response.data[2].cumple
                self.nocumple = response.data[2].total - response.data[2].cumple
                $("#nameReport").text('Sanos');

                setTimeout(function() {
                    $('table').trigger('footable_redraw');
                    $('.chart').data('easyPieChart').update(response.data[2].avance);
                }, 100);
            }).catch(e => {
                this.errors.push(e)
            })
        },

        Micheck: function(){
            if(this.reportNom == true){
                $("#nameReport").text('Prematuros');
                this.tb_prematuro = true
                this.tb_sano = false
            }else{
                $("#nameReport").text('Sanos');
                this.tb_sano = true
                this.tb_prematuro = false
            }
        },

        PrintExcel(e) {
            let prov = $("#provincia").val();
            let dist = $("#distrito").val();
            url_ = window.location.origin + window.location.pathname + 'print/?sector='+this.sector+'&prov='+prov+'&dist='+dist+'&anio='+this.anio+'&mes='+this.mes+'&type='+e;
            window.open(url_, '_parent');
        },
    },
})