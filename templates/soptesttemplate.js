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
        if (["number", "string", "boolean"].includes(attrs[i].type)) {
            cowTextArray[2] = "y";
            try {
                let a = eval(attrs[i].ref);
            }
            catch(error) {
                cowTextArray[2] = "n";
            }
        }
        else if (["function", "object"].includes(attrs[i].type)) {
            cowTextArray[2] = "n.a.";
        }
        else if (attrs[i].type == "function") {
            cowTextArray[2] = "n.a.";
        }

        cowTextArray[3] = "blank";

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