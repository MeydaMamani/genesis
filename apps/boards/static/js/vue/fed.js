new Vue({
    delimiters: ['[[', ']]'],
    el:'#tablerofed',
    data:{
        lists: [],
        errors: [],
        listDistrictKids: [],
        listDistrictPreg: [],
    },
    created:function(){

    },
    methods:{
        filterDistKids(e) {
            axios.get('filterDist/', { params: { id: e.target.value } })
            .then(respuesta => {
                this.listDistrictKids = respuesta.data
            });
        },

        searchKids() {
            let prov = $("#provincia").val();
            let dist = $("#distrito").val();

            axios.get('child/', { params: { prov: prov, dist: dist } })
            .then(respuesta => {
                let child = respuesta.data

                var nMonthChild = []; var dmc03 = []; var dSi0201 = []; var dSi0202 = []; var dSi0203 = []; var dSi03 = [];
                for (i = 0; i < child.length; i++) {
                    nMonthChild.push(child[i].nombremes);
                    dmc03.push(child[i].av_pqtrn);
                    dSi0201.push(child[i].av_si0201);
                    dSi0202.push(child[i].av_si0202);
                    dSi0203.push(child[i].av_si0203);
                    dSi03.push(child[i].av_si03);
                }

                var dPqtRn = {
                    label: 'MC03',
                    data: dmc03,
                    backgroundColor: ['#19404063'],
                    borderColor: ['#19404063'],
                };

                var dSanoPrem = {
                    label: 'SI0201',
                    data: dSi0201,
                    backgroundColor: ['#9966ff4d'],
                    borderColor: ['#9966ff4d'],
                };

                var dAnemina = {
                    label: 'SI0202',
                    data: dSi0202,
                    backgroundColor: ['#c1ededc4'],
                    borderColor: ['#c1ededc4'],
                };

                var dSinAnemia = {
                    label: 'SI0203',
                    data: dSi0203,
                    backgroundColor: ['#0d6efd47'],
                    borderColor: ['#0d6efd47'],
                };

                var dCred = {
                    label: 'SI03',
                    data: dSi03,
                    backgroundColor: ['#0d13fd59'],
                    borderColor: ['#0d13fd59'],
                };

                $('#myChartChild').remove();
                $('.chartChild').append("<canvas id='myChartChild'></canvas>");
                var ctx_province = document.getElementById("myChartChild").getContext("2d");
                var myChartProvince = new Chart(ctx_province, {
                    type: "line",
                    data: {
                        labels: nMonthChild,
                        datasets: [ dPqtRn, dSanoPrem, dAnemina, dSinAnemia, dCred ]
                    },
                    plugins: [ChartDataLabels],
                    options: options,
                });
            });
        },

        filterDistPreg(e) {
            axios.get('filterDist/', { params: { id: e.target.value } })
            .then(respuesta => {
                this.listDistrictPreg = respuesta.data
            });
        },

        searchPregnant() {
            let prov = $("#provincia1").val();
            let dist = $("#distrito1").val();

            axios.get('preg/', { params: { prov: prov, dist: dist } })
            .then(respuesta => {
                let gest = respuesta.data

                var nMonthGest = []; var dSi01 = []; var dSi04 = []; var dVi0101 = []; var dVi0102 = []; var dVii01 = [];
                for (i = 0; i < gest.length; i++) {
                    nMonthGest.push(gest[i].nombremes);
                    dSi01.push(gest[i].av_si01);
                    dSi04.push(gest[i].av_si04);
                    dVi0101.push(gest[i].av_vi0101);
                    dVi0102.push(gest[i].av_vi0102);
                    dVii01.push(gest[i].av_vii01);
                }

                var dtSi01 = {
                    label: 'SI01',
                    data: dSi01,
                    backgroundColor: ['#ffb22b59'],
                    borderColor: ['#ffb22b59'],
                };

                var dtSi04 = {
                    label: 'SI04',
                    data: dSi04,
                    backgroundColor: ['#f236752b'],
                    borderColor: ['#f236752b'],
                };

                var dtVi0101 = {
                    label: 'VI0101',
                    data: dVi0101,
                    backgroundColor: ['#ecd6c0e3'],
                    borderColor: ['#ecd6c0e3'],
                };

                var dtVi0102 = {
                    label: 'VI0102',
                    data: dVi0102,
                    backgroundColor: ['#C0EDC6'],
                    borderColor: ['#C0EDC6'],
                };

                var dtVii01 = {
                    label: 'VII01',
                    data: dVii01,
                    backgroundColor: ['#CEC0ED'],
                    borderColor: ['#CEC0ED'],
                };

                $('#myChartGest').remove();
                $('.chartGest').append("<canvas id='myChartGest'></canvas>");
                var ctx_province = document.getElementById("myChartGest").getContext("2d");
                var myChartProvince = new Chart(ctx_province, {
                    type: "line",
                    data: {
                        labels: nMonthGest,
                        datasets: [ dtSi01, dtSi04, dtVi0101, dtVi0102, dtVii01 ]
                    },
                    plugins: [ChartDataLabels],
                    options: options,
                });
            });
        },
    },
})