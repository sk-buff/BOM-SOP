function getResTable() {
    var attrs = eval({{ jsonData }});
    var table = document.createElement('table');
    table.setAttribute('border', '1');

    var headLine = document.createElement('tr');
    var headCowArray = ['attribute', 'type', 'read', 'write'];
    for (let i = 0; i < 4; i++) {
        let headCow = document.createElement('th');
        let text = document.createTextNode(headCowArray[i]);
        headCow.appendChild(text);
        headLine.appendChild(headCow);
    }
    table.appendChild(headLine);

    var len = attrs.length;
    for (let i = 0; i < len; i++) {
        let row = document.createElement('tr');
        
        let cowTextArray = [attrs[i].ref, attrs[i].type];
        if (["number", "string", "boolean", "function"].includes(attrs[i].type)) {
            cowTextArray[2] = "y";
            try {
                let a = eval(attrs[i].ref);
            }
            catch(error) {
                cowTextArray[2] = "n";
            }
        }
        else if (["undefined", "object"].includes(attrs[i].type)) {
            cowTextArray[2] = "n.a.";
        }

        if (["number", "string", "boolean", "function"].includes(attrs[i].type)) {
            cowTextArray[3] = "y";

            let assignValue;
            if (attrs[i].type == "number") {
                assignValue = "0";
            }
            else if (attrs[i].type == "string") {
                assignValue = "'abc'";
            }
            else if (attrs[i].type == "boolean") {
                assignValue = "true";
            }
            else if (attrs[i].type == "function") {
                assignValue = "function () { return; }"
            }

            try {
                eval(attrs[i].ref + "=" + assignValue);
            }
            catch (error) {
                cowTextArray[3] = "n";
            }
        }
        else if (["undefined", "object"].includes(attrs[i].type)) {
            cowTextArray[3] = "n.a.";
        }

        for (let j = 0; j < 4; j++) {
            let cow = document.createElement('td');
            let text = document.createTextNode(cowTextArray[j]);
            cow.appendChild(text);
            row.appendChild(cow);
        }

        table.appendChild(row);
    }

    return table;
}