new Vue({
    delimiters: ['[[', ']]'],
    el:'#appPadronNom',
    data:{
        lists: [],
        listDistricts: [],
        listActas: [],
        errors: [],
        anio: 0,
        mes: 0,
        total: 0,
        cumple: 0,
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

            if(this.anio == 0){
                this.anio = new Date().getFullYear();
            }
            if(this.mes == 0){
                this.mes = new Date().getMonth()+1;
            }
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
            let valoresCheck = [];
            $("input[type=checkbox]:checked").each(function(){ valoresCheck.push(this.value).toString(); });
            formData.set('mes', valoresCheck);
            axios({
                headers: { 'X-CSRFToken': csrfmiddlewaretoken, 'Content-Type': 'multipart/form-data' },
                method: 'POST',
                url: 'list/',
                data: formData
            }).then(response => {
                self.lists = response.data
                self.total = response.data[0].total
                self.cumple = response.data[0].cumple
                setTimeout(function() {
                    $('table').trigger('footable_redraw');
                    $('.chart').data('easyPieChart').update(response.data[0].avance);
                }, 100);
            }).catch(e => {
                this.errors.push(e)
            })
        },

        PrintSello() {
            let prov = $("#provincia").val();
            let dist = $("#distrito").val();
            let seg = $("#seguro").val();
            let valoresCheck = [];
            $("input[type=checkbox]:checked").each(function(){ valoresCheck.push(this.value.toString()); });
            url_ = window.location.origin + window.location.pathname + 'print/?prov='+prov+'&dist='+dist+'&seguro='+seg+'&mes='+valoresCheck;
            window.open(url_, '_parent');
        },

        ActasHomol: function(){
            axios.get('actas/')
            .then(respuesta => {
                this.listActas = respuesta.data
            });
        },

        PrintPadron() {
            let prov = $("#provincia1").val();
            let dist = $("#distrito1").val();
            url_ = window.location.origin + window.location.pathname + 'padronNom/?prov='+prov+'&dist='+dist+'&anio='+this.anio+'&mes='+this.mes;
            window.open(url_, '_parent');
        },
    },
})