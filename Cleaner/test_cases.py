'''
Test cases needed for the unittesting
Each test is a tuple:
    [0] - Input
    [1] - Expected Output
'''


script_test = (

    '''
    <script type="text/javascript">
        //<![CDATA[
        var i = 10;
        if (i < 5) {
        // some code
        }
        //]]>
    </script>
    ''',


    ''''''
)


empty_tags = (
    '''
    <div>
        <div>

        </div>
    </div>

    <p></p>

    <h2></h2>
    <h1>
    ''',


    ''''''
)


comment_test = (
    '''
    <!-- Favicon -->
    <!--[if IE 9]>
    <style type="text/css">
      * {
        filter: none !important;
      }
    </style>
	<![endif]-->
    ''',


    ''''''
)


arab_and_comment = (
    '''<li id="lang-list-tab3" aria-selected="false" role="tab" aria-controls="lang-tab3">
                         <!-- <a href="#lang-tab3" title="Europe Tab">-->
                         <span class="region-title"><span class="icon-arrow-down"></span>اوروبا<span class="text-hide">tab</span></span>
                         <span class="region-image"></span>
                          <!--</a>-->
                      </li>
    ''',

    '''<html><body>
                <li aria-controls="lang-tab3" aria-selected="false" id="lang-list-tab3" role="tab">
                         <span class="region-title">اوروبا<span class="text-hide">tab</span></span>
                </li>
    </body></html>
    '''
)
