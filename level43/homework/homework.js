
        function getSelectedRadioValue() {
            const radios = document.getElementsByName('commentOption');
            for (let i = 0; i < radios.length; i++) {
                if (radios[i].checked) {
                    alert('You selected (Radio): ' + radios[i].value);
                    return;
                }
            }
            alert('No option selected (Radio)');
        }


        function getSelectedCheckboxValues() {
            const checkboxes = document.getElementsByName('commentOptions');
            let selectedValues = [];
            for (let i = 0; i < checkboxes.length; i++) {
                if (checkboxes[i].checked) {
                    selectedValues.push(checkboxes[i].value);
                }
            }
            if (selectedValues.length > 0) {
                alert('You selected (Checkboxes): ' + selectedValues.join(', '));
            } else {
                alert('No options selected (Checkboxes)');
            }
        }

  
        function getSelectedDropDownValue() {
            const select = document.getElementById('commentSelect');
            alert('You selected (Drop-down): ' + select.value);
        }

        function testLogicalOperators() {
            let a = true;
            let b = false;
            
            alert('a && b: ' + (a && b)); 
            alert('a || b: ' + (a || b)); 
            alert('!a: ' + (!a));          
        }
        console.log(3 > 2)
