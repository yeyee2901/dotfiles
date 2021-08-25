<!DOCTYPE html>
<html>
    <head>
        <!-- Enable syntax highlighting -->
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/default.min.css" />
        <link rel="Stylesheet" type="text/css" href="%root_path%%css%">
        <title>%title%</title>
        <meta http-equiv="Content-Type" content="text/html; charset=%encoding%">
        <meta name="viewport" content="width=device-width, initial-scale=1">

    </head>
    <body>
    %content%

        <!-- include highlight.js -->
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/highlight.min.js"></script>
        <script type="text/javascript">
            document.querySelectorAll('pre').forEach(block => hljs.highlightBlock(block));
        </script>
    </body>
</html>
