<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
        <meta name="csrf-token" content="{{ csrf_token() }}">
        <title>{{ __('DEIT - PASCO') }}</title>
        <link rel="apple-touch-icon" sizes="76x76" href="{{ asset('img') }}/logo.jpg">
        <link rel="icon" type="image/png" href="{{ asset('img') }}/logo.jpg">
        <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no' name='viewport' />

        <!-- Google Font: Source Sans Pro -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
        <!-- Font Awesome -->
        <link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css">
        <!-- Ionicons -->
        <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
        <!-- Tempusdominus Bootstrap 4 -->
        <link rel="stylesheet" href="plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css">
        <!-- iCheck -->
        <link rel="stylesheet" href="plugins/icheck-bootstrap/icheck-bootstrap.min.css">
        <!-- JQVMap -->
        <link rel="stylesheet" href="plugins/jqvmap/jqvmap.min.css">
        <!-- Theme style -->
        <link rel="stylesheet" href="dist/css/adminlte.min.css">
        <!-- overlayScrollbars -->
        <link rel="stylesheet" href="plugins/overlayScrollbars/css/OverlayScrollbars.min.css">
        <!-- Daterange picker -->
        <link rel="stylesheet" href="plugins/daterangepicker/daterangepicker.css">
        <!-- summernote -->
        <link rel="stylesheet" href="plugins/summernote/summernote-bs4.min.css">

        <!-- Select2 -->
        <link rel="stylesheet" href="plugins/select2/css/select2.min.css">
        <link rel="stylesheet" href="plugins/select2-bootstrap4-theme/select2-bootstrap4.min.css">

        <!-- Toastr -->
        <link rel="stylesheet" href="plugins/toastr/toastr.min.css">

        <!-- SweetAlert2 -->
        <link rel="stylesheet" href="plugins/sweetalert2-theme-bootstrap-4/bootstrap-4.min.css">

        <link rel="stylesheet" href="{{ asset('./css/styleFed.css') }}"/>
        <link rel="stylesheet" href="{{ asset('./css/style.css') }}"/>

        <!-- link paginacion -->
        <link rel="stylesheet" href="./plugins/footable/css/footable.core.css">
        <link rel="stylesheet" href="./css/style_footable.css">

        <!-- jQuery -->
        <script src="plugins/jquery/jquery.min.js"></script>

        <!-- VUE -->
        <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
        <script src="./plugins/vue/vue.js"></script>

        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-select@1.13.14/dist/css/bootstrap-select.min.css">

        <!-- link para iconos -->
        <link rel="stylesheet" href="./css/materialdesignicons.css">
        <link rel="stylesheet" href="./css/materialdesignicons.min.css">

        <!-- estilos css -->
        <link rel="stylesheet" href="{{ asset('./css/styleVaccine.css') }}"/>
        <link rel="stylesheet" href="{{ asset('./css/stylePregnant.css') }}"/>
        <script src="./js/hammer/hammer.min.js"></script>

        @yield('css')
    </head>
    <body class="hold-transition sidebar-mini layout-fixed">
        <div class="wrapper">
            <!-- Preloader -->
            <div class="preloader flex-column justify-content-center align-items-center">
                <img class="animation__shake" src="dist/img/AdminLTELogo.png" alt="AdminLTELogo" height="60" width="60">
            </div>
            @include('layouts.navbars.navs.auth')

            @include('layouts.navbars.sidebar')

            @yield('content')
            @include('layouts.footer.auth')
        </div>
        <!-- ./wrapper -->
        <!-- jQuery UI 1.11.4 -->
        <script src="plugins/jquery-ui/jquery-ui.min.js"></script>
        <!-- Resolve conflict in jQuery UI tooltip with Bootstrap tooltip -->
        <script>
        $.widget.bridge('uibutton', $.ui.button)
        </script>
        <!-- Bootstrap 4 -->
        <script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
        <!-- ChartJS -->
        <script src="plugins/chart.js/Chart.min.js"></script>
        <!-- Sparkline -->
        <script src="plugins/sparklines/sparkline.js"></script>
        <!-- JQVMap -->
        {{-- <script src="plugins/jqvmap/jquery.vmap.min.js"></script> --}}
        {{-- <script src="plugins/jqvmap/maps/jquery.vmap.usa.js"></script> --}}
        <!-- jQuery Knob Chart -->
        <script src="plugins/jquery-knob/jquery.knob.min.js"></script>
        <!-- daterangepicker -->
        <script src="plugins/moment/moment.min.js"></script>
        <script src="plugins/daterangepicker/daterangepicker.js"></script>
        <!-- Tempusdominus Bootstrap 4 -->
        <script src="plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.min.js"></script>
        <!-- Summernote -->
        <script src="plugins/summernote/summernote-bs4.min.js"></script>
        <!-- overlayScrollbars -->
        <script src="plugins/overlayScrollbars/js/jquery.overlayScrollbars.min.js"></script>
        <!-- AdminLTE App -->
        <script src="dist/js/adminlte.js"></script>
        <!-- AdminLTE for demo purposes -->
        <script src="dist/js/demo.js"></script>
        <!-- AdminLTE dashboard demo (This is only for demo purposes) -->
        <script src="dist/js/pages/dashboard.js"></script>
        <!-- SweetAlert2 -->
        <script src="plugins/sweetalert2/sweetalert2.min.js"></script>
        <!-- Select2 -->
        <script src="plugins/select2/js/select2.full.min.js"></script>
        <script>
            $('.select2').select2();
        </script>

        <script src="./plugins/footable/js/footable-init.js"></script>
        <script src="./plugins/footable/js/footable.all.min.js"></script>
        <!-- Toastr -->
        <script src="./plugins/toastr/toastr.min.js"></script>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap-select@1.13.14/dist/js/bootstrap-select.min.js"></script>

        @yield('javascript')
    </body>
</html>
