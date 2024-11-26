new Vue({
    delimiters: ['[[', ']]'],
    el:'#appPlano',
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

        listEstab(e) {
            axios.get('filterEstab/', { params: { id: e.target.value } })
            .then(respuesta => {
                this.listEess = respuesta.data
            });
        },

        PrintPlano() {
            let prov = $("#provincia").val();
            let dist = $("#distrito").val();
            if(prov == 0){
                $.toast({
                    heading: '¡Seleccione Provincia!',
                    position: 'top-right',
                    loaderBg:'#ff6849',
                    icon: 'error',
                    hideAfter: 3000,
                    stack: 6
                });
            }
            else if(dist == 0){
                $.toast({
                    heading: '¡Seleccione Distrito!',
                    position: 'top-right',
                    loaderBg:'#ff6849',
                    icon: 'error',
                    hideAfter: 3000,
                    stack: 6
                });
            }
            else{
                let eess = $("#eess").val();
                let ups = $("#ups").val();
                url_ = window.location.origin + window.location.pathname + 'print/?prov='+prov+'&dist='+dist+'&eess='+eess+'&ups='+ups+'&anio='+this.anio+'&mes='+this.mes;
                window.open(url_, '_parent');
            }
        },
    },
})