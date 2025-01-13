new Vue({
    delimiters: ['[[', ']]'],
    el:'#appSetipress',
    data:{
        lists: [],
        listDistricts: [],
        listEess: [],
        errors: [],
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
            if(this.anio == 0){ this.anio = new Date().getFullYear();}
            if(this.mes == 0){ this.mes = new Date().getMonth()+1; }
        },

        listDistritos(e) {
            axios.get('filterDist/', { params: { id: e.target.value } })
            .then(respuesta => {
                this.listDistricts = respuesta.data
            });
        },

        listEstab(e) {
            axios.get('filterEstab/', { params: { id: e.target.value } })
            .then(respuesta => {
                this.listEess = respuesta.data
            });
        },

        PrintExcel() {
            let dist = $("#distrito").val();
            let eess = $("#establecimiento").val();
            let tipo = $("#tipo").val();
            url_ = window.location.origin + window.location.pathname + 'print/?dist='+dist+'&anio='+this.anio+'&mes='+this.mes+'&eess='+eess+'&tipo='+tipo;
            window.open(url_, '_parent');
        },
    },
})