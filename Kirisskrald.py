    #tags
        tags ='''   <input type='radio' id='yes' name='tag' value='Yes'> <label for='yes'>Yes</label><br>
                    <input type='radio' id='maybe' name='tag' value='Maybe'> <label for='maybe'>Maybe</label><br>
                    <input type='radio' id='no' name='tag' value='No'> <label for="no">No</label><br>
        '''

        notes = '''<form><label for="fname">Notes:</label><br><input type="text" id="fname" name="fname"><br>
        '''



        with Grid("1 1 1") as grid: 
            grid.cell("a", 1, 2, 1, 3).markdown(image)
            grid.cell("b", 2, 3, 1, 2).markdown(Text1)
            grid.cell("c", 2, 3, 2, 3).markdown(notes)
            grid.cell("d", 3, 4, 2, 3).plotly_chart(get_plotly_fig())
            grid.cell("e", 3, 4, 1, 2).markdown(tags)
