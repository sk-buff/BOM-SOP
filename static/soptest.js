function getResTable() {
    var attrs = eval([{"type":"function","ref":"window.opener.close"},{"type":"function","ref":"window.opener.stop"},{"type":"function","ref":"window.opener.focus"},{"type":"function","ref":"window.opener.blur"},{"type":"function","ref":"window.opener.open"},{"type":"function","ref":"window.opener.alert"},{"type":"function","ref":"window.opener.confirm"},{"type":"function","ref":"window.opener.prompt"},{"type":"function","ref":"window.opener.print"},{"type":"function","ref":"window.opener.postMessage"},{"type":"function","ref":"window.opener.captureEvents"},{"type":"function","ref":"window.opener.releaseEvents"},{"type":"function","ref":"window.opener.getSelection"},{"type":"function","ref":"window.opener.getComputedStyle"},{"type":"function","ref":"window.opener.matchMedia"},{"type":"function","ref":"window.opener.moveTo"},{"type":"function","ref":"window.opener.moveBy"},{"type":"function","ref":"window.opener.resizeTo"},{"type":"function","ref":"window.opener.resizeBy"},{"type":"function","ref":"window.opener.scroll"},{"type":"function","ref":"window.opener.scrollTo"},{"type":"function","ref":"window.opener.scrollBy"},{"type":"function","ref":"window.opener.requestAnimationFrame"},{"type":"function","ref":"window.opener.cancelAnimationFrame"},{"type":"function","ref":"window.opener.getDefaultComputedStyle"},{"type":"function","ref":"window.opener.scrollByLines"},{"type":"function","ref":"window.opener.scrollByPages"},{"type":"function","ref":"window.opener.sizeToContent"},{"type":"function","ref":"window.opener.updateCommands"},{"type":"function","ref":"window.opener.find"},{"type":"function","ref":"window.opener.dump"},{"type":"function","ref":"window.opener.setResizable"},{"type":"function","ref":"window.opener.requestIdleCallback"},{"type":"function","ref":"window.opener.cancelIdleCallback"},{"type":"function","ref":"window.opener.btoa"},{"type":"function","ref":"window.opener.atob"},{"type":"function","ref":"window.opener.setTimeout"},{"type":"function","ref":"window.opener.clearTimeout"},{"type":"function","ref":"window.opener.setInterval"},{"type":"function","ref":"window.opener.clearInterval"},{"type":"function","ref":"window.opener.queueMicrotask"},{"type":"function","ref":"window.opener.createImageBitmap"},{"type":"function","ref":"window.opener.fetch"},{"type":"string","ref":"window.opener.name"},{"type":"object","ref":"window.opener.history"},{"type":"object","ref":"window.opener.customElements"},{"type":"object","ref":"window.opener.locationbar"},{"type":"object","ref":"window.opener.menubar"},{"type":"object","ref":"window.opener.personalbar"},{"type":"object","ref":"window.opener.scrollbars"},{"type":"object","ref":"window.opener.statusbar"},{"type":"object","ref":"window.opener.toolbar"},{"type":"string","ref":"window.opener.status"},{"type":"boolean","ref":"window.opener.closed"},{"type":"undefined","ref":"window.opener.event"},{"type":"number","ref":"window.opener.length"},{"type":"object","ref":"window.opener.opener"},{"type":"object","ref":"window.opener.frameElement"},{"type":"object","ref":"window.opener.navigator"},{"type":"object","ref":"window.opener.external"},{"type":"object","ref":"window.opener.screen"},{"type":"number","ref":"window.opener.innerWidth"},{"type":"number","ref":"window.opener.innerHeight"},{"type":"number","ref":"window.opener.scrollX"},{"type":"number","ref":"window.opener.pageXOffset"},{"type":"number","ref":"window.opener.scrollY"},{"type":"number","ref":"window.opener.pageYOffset"},{"type":"number","ref":"window.opener.screenLeft"},{"type":"number","ref":"window.opener.screenTop"},{"type":"number","ref":"window.opener.screenX"},{"type":"number","ref":"window.opener.screenY"},{"type":"number","ref":"window.opener.outerWidth"},{"type":"number","ref":"window.opener.outerHeight"},{"type":"object","ref":"window.opener.performance"},{"type":"number","ref":"window.opener.mozInnerScreenX"},{"type":"number","ref":"window.opener.mozInnerScreenY"},{"type":"number","ref":"window.opener.devicePixelRatio"},{"type":"number","ref":"window.opener.scrollMaxX"},{"type":"number","ref":"window.opener.scrollMaxY"},{"type":"boolean","ref":"window.opener.fullScreen"},{"type":"object","ref":"window.opener.ondevicemotion"},{"type":"object","ref":"window.opener.ondeviceorientation"},{"type":"object","ref":"window.opener.onabsolutedeviceorientation"},{"type":"object","ref":"window.opener.ondeviceproximity"},{"type":"object","ref":"window.opener.onuserproximity"},{"type":"object","ref":"window.opener.ondevicelight"},{"type":"object","ref":"window.opener.InstallTrigger"},{"type":"object","ref":"window.opener.sidebar"},{"type":"object","ref":"window.opener.crypto"},{"type":"object","ref":"window.opener.onabort"},{"type":"object","ref":"window.opener.onblur"},{"type":"object","ref":"window.opener.onfocus"},{"type":"object","ref":"window.opener.onauxclick"},{"type":"object","ref":"window.opener.oncanplay"},{"type":"object","ref":"window.opener.oncanplaythrough"},{"type":"object","ref":"window.opener.onchange"},{"type":"object","ref":"window.opener.onclick"},{"type":"object","ref":"window.opener.onclose"},{"type":"object","ref":"window.opener.oncontextmenu"},{"type":"object","ref":"window.opener.oncuechange"},{"type":"object","ref":"window.opener.ondblclick"},{"type":"object","ref":"window.opener.ondrag"},{"type":"object","ref":"window.opener.ondragend"},{"type":"object","ref":"window.opener.ondragenter"},{"type":"object","ref":"window.opener.ondragexit"},{"type":"object","ref":"window.opener.ondragleave"},{"type":"object","ref":"window.opener.ondragover"},{"type":"object","ref":"window.opener.ondragstart"},{"type":"object","ref":"window.opener.ondrop"},{"type":"object","ref":"window.opener.ondurationchange"},{"type":"object","ref":"window.opener.onemptied"},{"type":"object","ref":"window.opener.onended"},{"type":"object","ref":"window.opener.onformdata"},{"type":"object","ref":"window.opener.oninput"},{"type":"object","ref":"window.opener.oninvalid"},{"type":"object","ref":"window.opener.onkeydown"},{"type":"object","ref":"window.opener.onkeypress"},{"type":"object","ref":"window.opener.onkeyup"},{"type":"object","ref":"window.opener.onload"},{"type":"object","ref":"window.opener.onloadeddata"},{"type":"object","ref":"window.opener.onloadedmetadata"},{"type":"object","ref":"window.opener.onloadend"},{"type":"object","ref":"window.opener.onloadstart"},{"type":"object","ref":"window.opener.onmousedown"},{"type":"object","ref":"window.opener.onmouseenter"},{"type":"object","ref":"window.opener.onmouseleave"},{"type":"object","ref":"window.opener.onmousemove"},{"type":"object","ref":"window.opener.onmouseout"},{"type":"object","ref":"window.opener.onmouseover"},{"type":"object","ref":"window.opener.onmouseup"},{"type":"object","ref":"window.opener.onwheel"},{"type":"object","ref":"window.opener.onpause"},{"type":"object","ref":"window.opener.onplay"},{"type":"object","ref":"window.opener.onplaying"},{"type":"object","ref":"window.opener.onprogress"},{"type":"object","ref":"window.opener.onratechange"},{"type":"object","ref":"window.opener.onreset"},{"type":"object","ref":"window.opener.onresize"},{"type":"object","ref":"window.opener.onscroll"},{"type":"object","ref":"window.opener.onseeked"},{"type":"object","ref":"window.opener.onseeking"},{"type":"object","ref":"window.opener.onselect"},{"type":"object","ref":"window.opener.onshow"},{"type":"object","ref":"window.opener.onstalled"},{"type":"object","ref":"window.opener.onsubmit"},{"type":"object","ref":"window.opener.onsuspend"},{"type":"object","ref":"window.opener.ontimeupdate"},{"type":"object","ref":"window.opener.onvolumechange"},{"type":"object","ref":"window.opener.onwaiting"},{"type":"object","ref":"window.opener.onselectstart"},{"type":"object","ref":"window.opener.ontoggle"},{"type":"object","ref":"window.opener.onpointercancel"},{"type":"object","ref":"window.opener.onpointerdown"},{"type":"object","ref":"window.opener.onpointerup"},{"type":"object","ref":"window.opener.onpointermove"},{"type":"object","ref":"window.opener.onpointerout"},{"type":"object","ref":"window.opener.onpointerover"},{"type":"object","ref":"window.opener.onpointerenter"},{"type":"object","ref":"window.opener.onpointerleave"},{"type":"object","ref":"window.opener.ongotpointercapture"},{"type":"object","ref":"window.opener.onlostpointercapture"},{"type":"object","ref":"window.opener.onmozfullscreenchange"},{"type":"object","ref":"window.opener.onmozfullscreenerror"},{"type":"object","ref":"window.opener.onanimationcancel"},{"type":"object","ref":"window.opener.onanimationend"},{"type":"object","ref":"window.opener.onanimationiteration"},{"type":"object","ref":"window.opener.onanimationstart"},{"type":"object","ref":"window.opener.ontransitioncancel"},{"type":"object","ref":"window.opener.ontransitionend"},{"type":"object","ref":"window.opener.ontransitionrun"},{"type":"object","ref":"window.opener.ontransitionstart"},{"type":"object","ref":"window.opener.onwebkitanimationend"},{"type":"object","ref":"window.opener.onwebkitanimationiteration"},{"type":"object","ref":"window.opener.onwebkitanimationstart"},{"type":"object","ref":"window.opener.onwebkittransitionend"},{"type":"object","ref":"window.opener.onerror"},{"type":"object","ref":"window.opener.speechSynthesis"},{"type":"object","ref":"window.opener.onafterprint"},{"type":"object","ref":"window.opener.onbeforeprint"},{"type":"object","ref":"window.opener.onbeforeunload"},{"type":"object","ref":"window.opener.onhashchange"},{"type":"object","ref":"window.opener.onlanguagechange"},{"type":"object","ref":"window.opener.onmessage"},{"type":"object","ref":"window.opener.onmessageerror"},{"type":"object","ref":"window.opener.onoffline"},{"type":"object","ref":"window.opener.ononline"},{"type":"object","ref":"window.opener.onpagehide"},{"type":"object","ref":"window.opener.onpageshow"},{"type":"object","ref":"window.opener.onpopstate"},{"type":"object","ref":"window.opener.onrejectionhandled"},{"type":"object","ref":"window.opener.onstorage"},{"type":"object","ref":"window.opener.onunhandledrejection"},{"type":"object","ref":"window.opener.onunload"},{"type":"object","ref":"window.opener.localStorage"},{"type":"string","ref":"window.opener.origin"},{"type":"boolean","ref":"window.opener.crossOriginIsolated"},{"type":"boolean","ref":"window.opener.isSecureContext"},{"type":"object","ref":"window.opener.indexedDB"},{"type":"object","ref":"window.opener.caches"},{"type":"object","ref":"window.opener.sessionStorage"},{"type":"string","ref":"window.opener.document.location.href"},{"type":"string","ref":"window.opener.document.location.origin"},{"type":"string","ref":"window.opener.document.location.protocol"},{"type":"string","ref":"window.opener.document.location.host"},{"type":"string","ref":"window.opener.document.location.hostname"},{"type":"string","ref":"window.opener.document.location.port"},{"type":"string","ref":"window.opener.document.location.pathname"},{"type":"string","ref":"window.opener.document.location.search"},{"type":"string","ref":"window.opener.document.location.hash"},{"type":"function","ref":"window.opener.document.location.assign"},{"type":"function","ref":"window.opener.document.location.replace"},{"type":"function","ref":"window.opener.document.location.reload"},{"type":"function","ref":"window.opener.document.location.toString"},{"type":"string","ref":"window.opener.location.href"},{"type":"string","ref":"window.opener.location.origin"},{"type":"string","ref":"window.opener.location.protocol"},{"type":"string","ref":"window.opener.location.host"},{"type":"string","ref":"window.opener.location.hostname"},{"type":"string","ref":"window.opener.location.port"},{"type":"string","ref":"window.opener.location.pathname"},{"type":"string","ref":"window.opener.location.search"},{"type":"string","ref":"window.opener.location.hash"},{"type":"function","ref":"window.opener.location.assign"},{"type":"function","ref":"window.opener.location.replace"},{"type":"function","ref":"window.opener.location.reload"},{"type":"function","ref":"window.opener.location.toString"}]);
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