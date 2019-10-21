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


