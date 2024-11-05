new Vue({
    delimiters: ['[[', ']]'],
    el:'#appPromsa',
    data:{
        lists: [],
        listDistricts: [],
        listEess: [],
        errors: [],
        anio: 0,
    },
    created:function(){
        this.listYears();
    },
    methods:{
        listYears: function(){
            let fec = new Date();
            var selectYear = document.getElementById("anio");
            for(var i = 2024; i<=fec.getFullYear(); i++)selectYear.options.add(new Option(i,i));
            if(this.anio == 0){ this.anio = new Date().getFullYear(); }
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
            let prov = $("#provincia").val();
            let dist = $("#distrito").val();
            let eess = $("#establecimiento").val();
            let tipo = $("#tipo").val();
            url_ = window.location.origin + window.location.pathname + 'print/?prov='+prov+'&dist='+dist+'&anio='+this.anio+'&eess='+eess+'&tipo='+tipo;
            window.open(url_, '_parent');
        },
    },
})