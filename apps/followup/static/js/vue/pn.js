new Vue({
    delimiters: ['[[', ']]'],
    el:'#appPadronNom',
    data:{
        lists: [],
        listDistricts: [],
        listActas: [],
        errors: [],
        total: 0,
        cumple: 0,
    },
    created:function(){

    },
    methods:{
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
            url_ = window.location.origin + window.location.pathname + 'padronNom/?prov='+prov+'&dist='+dist;
            window.open(url_, '_parent');
        },
    },
})