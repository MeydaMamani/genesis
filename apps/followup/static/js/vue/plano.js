new Vue({
    delimiters: ['[[', ']]'],
    el:'#appPlano',
    data:{
        lists: [],
        listDistricts: [],
        listDistr40: [],
        listEess: [],
        listeessr40: [],
        errors: [],
        anio: 0,
        mes: 0,
        anio1: 0,
        mes1: 0,
        anioIni: 2023,
        mesIni: 1,
        anioFin: 0,
        mesFin: 0,
        anio2: 0,
        mes2: 0,
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
            var selectYear1 = document.getElementById("anio1");
            for(var i = 2024; i<=fec.getFullYear(); i++)selectYear1.options.add(new Option(i,i));
            var selectMonth1 = document.getElementById("mes1");
            for(var i = 1; i<=12; i++)selectMonth1.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));
            var selectYear2 = document.getElementById("anioIni");
            for(var i = 2023; i<=fec.getFullYear(); i++)selectYear2.options.add(new Option(i,i));
            var selectMonth2 = document.getElementById("mesIni");
            for(var i = 1; i<=12; i++)selectMonth2.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));
            var selectYear3 = document.getElementById("anioFin");
            for(var i = 2023; i<=fec.getFullYear(); i++)selectYear3.options.add(new Option(i,i));
            var selectMonth3 = document.getElementById("mesFin");
            for(var i = 1; i<=12; i++)selectMonth3.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));
            var selectYear4 = document.getElementById("anio2");
            for(var i = 2023; i<=fec.getFullYear(); i++)selectYear4.options.add(new Option(i,i));
            var selectMonth4 = document.getElementById("mes2");
            for(var i = 1; i<=12; i++)selectMonth4.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));
            selectMonth4.options.add(new Option('TODOS', 'TODOS'));

            if(this.anio == 0 || this.anio1 == 0 || this.anio2 == 0 || this.anioFin == 0){
                this.anio = new Date().getFullYear();
                this.anio1 = new Date().getFullYear();
                this.anioFin = new Date().getFullYear();
                this.anio2 = new Date().getFullYear();
            }
            if(this.mes == 0 || this.mes1 == 0 || this.mes2 == 0 || this.mesFin == 0){
                this.mes = new Date().getMonth()+1;
                this.mes1 = new Date().getMonth()+1;
                this.mesFin = new Date().getMonth()+1;
                this.mes2 = new Date().getMonth()+1;
            }
        },

        listDistritos(e) {
            axios.get('filterDist/', { params: { id: e.target.value } })
            .then(respuesta => {
                this.listDistricts = respuesta.data
            });
        },

        listDistR40(e) {
            axios.get('filterDist/', { params: { id: e.target.value } })
            .then(respuesta => {
                this.listDistr40 = respuesta.data
            });
        },

        listEstab(e) {
            axios.get('filterEstab/', { params: { id: e.target.value } })
            .then(respuesta => {
                this.listEess = respuesta.data
            });
        },

        listEstabR40(e) {
            axios.get('filterEstab/', { params: { id: e.target.value } })
            .then(respuesta => {
                this.listeessr40 = respuesta.data
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

        PrintR40Prof(){
            let prov = $("#provincia1").val();
            let dist = $("#distrito1").val();
            let eess = $("#eess1").val();
            let prof = $("#prof").val();
            url_ = window.location.origin + window.location.pathname + 'printR40Prof/?prov='+prov+'&dist='+dist+'&eess='+eess+'&prof='+prof+'&anio='+this.anio1+'&mes='+this.mes1;
            window.open(url_, '_parent');
        },

        PrintR40Doc(){
            let doc = $("#dni").val();
            url_ = window.location.origin + window.location.pathname + 'printR40Doc/?doc='+doc+'&anioIni='+this.anioIni+'&mesIni='+this.mesIni+'&anioFin='+this.anioFin+'&mesFin='+this.mesFin;
            window.open(url_, '_parent');
        },

        PrintCnv(){
            let prov = $("#provincia2").val();
            let dist = $("#distrito2").val();
            url_ = window.location.origin + window.location.pathname + 'printCnv/?prov='+prov+'&dist='+dist+'&anio='+this.anio2+'&mes='+this.mes2;
            window.open(url_, '_parent');
        },
    },
})