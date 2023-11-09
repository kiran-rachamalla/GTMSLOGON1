$(function() {
      $('a#test').on('click', function(e) {
        e.preventDefault()
        $.getJSON('/background_process_test',
            function(data) {
          //do nothing
        });
        return false;
      });
    });

$("button[class ^= 'sample']").click(function(){
fetch('/open_sap_gui?' + new URLSearchParams({
    action: 'OPEN_GUI',
    system: this.className.split("_")[1]
})).then(response => response.json())
  });

$("button[class ^= 'server']").click(function(){
fetch('/open_sap_gui?' + new URLSearchParams({
    action: 'START',
    system: this.className.split("_")[1]
})).then(response => response.json())
    .then(data => {
        $( "div.container" ).replaceWith( data );
    })
  });
$("button[class ^= 'stop_server']").click(function(){
fetch('/open_sap_gui?' + new URLSearchParams({
    action: 'STOP_SERVER',
    system: this.className.split("_")[2]
})).then(response => response.json())
    .then(data => {
        $( "div.container" ).replaceWith( data );
    })
  });
$("button[class ^= 'client_save']").click(function(){
    system = this.className.split("_")[2]
    client = this.className.split("_")[3]
    name = system.concat(",",client,",username,")
    pass = system.concat(",",client,",password,")
    com = system.concat(",",client,",comment,")
    username = document.getElementById(name).value
    password = document.getElementById(pass).value
    comment = document.getElementById(com).value
fetch('/update_client_info?' + new URLSearchParams({
    system : system,
    client : client,
    username : username,
    password : password,
    comment : comment
})).then(response => response.json()) });

function myFunction_copy(x) {
  // Get the text field
		  var copyText = document.getElementById(x.id.split('_')[0].trim());

		  // Select the text field
		  copyText.select();
		  copyText.setSelectionRange(0, 99999); // For mobile devices

		   // Copy the text inside the text field
		  navigator.clipboard.writeText(copyText.value);
		}
		function myMouseover(x){
			x.style.height = "23px";
            x.style.width = "23px";
		}
		function myMouseout(x){
			x.style.height = "20px";
			x.style.width = "20px";
		}
		function myMouseover1(x){
			x.style.height = "23px";
            x.style.width = "23px";
		}
		function myMouseout1(x){
			x.style.height = "20px";
			x.style.width = "20px";
		}
var gv_sys_type, gv_filter;
function make_row_visible(ls_table_row) {
    // Temp
    // lt_table_header = table.getElementsByTagName("th");
    // if(lt_table_header){}
    // var obj_h = new Mark(lt_table_header);
    // obj_h.unmark;
    // }
    // var obj1 = new Mark(ls_table_row);

    // // First unmark the highlighted word or letter
    // obj1.unmark();

    // // Highlight letter or word
    // obj1.mark(
    //     gv_filter,
    //     { className: 'a' + gv_filter }
    // );
    // //  Temp
    ls_table_row.style.display = "";
}
function make_row_invisible(ls_table_row) {
    ls_table_row.style.display = "none";
}
function make_all_rows_visible(table, lv_visible) {
    if (!table)
        return;
    // if (table) {
    lt_table_row = table.getElementsByTagName("tr");
    var j;
    for (j = 0; j < lt_table_row.length; j++) {
        if (lv_visible)
            make_row_visible(lt_table_row[j]);
        else
            make_row_invisible(lt_table_row[j]);
    }
    // }
}
function is_data_exist_in_row(ls_table_row) {
    var td, txtValue;
    let k = 0;
    do {
        td = ls_table_row.getElementsByTagName("td")[k];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(gv_filter) > -1) {
                return true;
            }
        }
        k++;
    }
    while (k < 2);
}
function is_data_exists_in_table(table) {
    if (!table)
        return;
    // if (table) {
    lt_table_row = table.getElementsByTagName("tr");
    var j, k, lv_visible;
    for (j = 1; j < lt_table_row.length; j++) { // here started from j=1 because j=0 is clent and description headings
        if (is_data_exist_in_row(lt_table_row[j])) {
            make_row_visible(lt_table_row[j]);
            lv_visible = true;
        }
        else {
            make_row_invisible(lt_table_row[j]);
        }
    }
    return lv_visible;
    // }
}
// function myFunction() {
//     input = document.getElementById("search-input");
//     filter = input.value.toUpperCase();
//     div = document.getElementsByClassName("card");
//     for (i = 0; i < div.length; i++) {
//         table = div[i].getElementsByTagName("table")[0];
//         b = div[i].getElementsByTagName("b")[0];
//         txtValue = b.textContent || b.innerText;
//         if (txtValue.toUpperCase().indexOf(filter) > -1) {
//             div[i].style.display = "";
//             make_all_rows_visible(table, true);
//             continue;
//         }
//         else {
//             if (is_data_exists_in_table(table))
//                 div[i].style.display = "";
//             else
//                 div[i].style.display = "none";
//         }
//     }
// }
function myFunction() {
    input = document.getElementById("search-input");
    gv_filter = input.value.toUpperCase();
    div = document.getElementsByClassName("card");

    for (i = 0; i < div.length; i++) {
        table = div[i].getElementsByTagName("table")[0];
        // b = div[i].getElementsByTagName("b")[0];
        b = div[i].getElementsByClassName("header-title float-left")[0];

        // var obj = new Mark(b);
        // obj.unmark();
        span = b.getElementsByTagName("span")[0];
        if (gv_sys_type) {
            // span = b.getElementsByTagName("span")[0];
            if (span) {
                spanValue = span.textContent || span.innerText;
                if (spanValue) {
                    if (spanValue.toUpperCase().indexOf(gv_sys_type) <= -1) {
                        // // Temp
                        // var span_obj = new Mark(span);
                        // span_obj.unmark();
                            //

                        continue;
                    }
                }
            }
            //         // temp
            //         else{
            //             span = div[i].getElementsByTagName("span")[0];
            //             if(span)
            //             {
            //                 spanValue = span.textContent || span.innerText;
            // if (spanValue) {
            //     if (spanValue.toUpperCase().indexOf(gv_sys_type) <= -1) {
            //         continue;
            //     }
            // }
            //             }
            //         }
            //         // temp
        }
        // // Temp
    // if (span) {
    //     span_obj = new Mark(span);
    //     span_obj.unmark();
    // }

        txtValue = b.textContent || b.innerText;
        if (txtValue.toUpperCase().indexOf(gv_filter) > -1) {
            // Temp
            // var obj = new Mark(b);

            // // First unmark the highlighted word or letter
            // obj.unmark();

            // Highlight letter or word
            // obj.mark(
            //     gv_filter,
            //     { className: 'a' + gv_filter }
            // );
            //  Temp
            div[i].style.display = "";

            make_all_rows_visible(table, true);
            continue;
        }
        else {
            if (is_data_exists_in_table(table))
                div[i].style.display = "";
            else
                div[i].style.display = "none";
        }
    }
    // // // Temp
    // if (span) {
    //     var span_obj = new Mark(span);
    //     span_obj.unmark();
    // }

}
function show_system(lv_sys_type) {
    // var ID = [];
    // $("*").each(function() {
    //     if (this.id) {
    //         ID.push(this.id);
    //     }
    // });
    // filter = lv_sys_type.value.toUpperCase().
    gv_sys_type = lv_sys_type;
    div = document.getElementsByClassName("card");
    for (i = 0; i < div.length; i++) {
        table = div[i].getElementsByTagName("table")[0];
        if (!gv_sys_type) {
            if (!gv_filter) {
                div[i].style.display = "";
                make_all_rows_visible(table, true);
                continue;
            }
            else {
                // div = document.getElementsByClassName("card");
                // for (i = 0; i < div.length; i++) {
                //     table = div[i].getElementsByTagName("table")[0];
                b = div[i].getElementsByTagName("b")[0];
                if (!gv_sys_type) {
                    span = b.getElementsByTagName("span")[0];
                    if (span) {
                        spanValue = span.textContent || span.innerText;
                        if (spanValue) {
                            if (spanValue.toUpperCase().indexOf(gv_sys_type) <= -1) {
                                continue;
                            }
                        }
                    }
                    //

                    //
                }
                txtValue = b.textContent || b.innerText;
                if (txtValue.toUpperCase().indexOf(gv_filter) > -1) {
                    div[i].style.display = "";
                    make_all_rows_visible(table, true);
                    continue;
                }
                else {
                    if (is_data_exists_in_table(table))
                        div[i].style.display = "";
                    else
                        div[i].style.display = "none";
                }
                // }
            }
        }
        b = div[i].getElementsByTagName("b")[0];
        span = b.getElementsByTagName("span")[0];
        if (!span)
            continue;
        txtValue = span.textContent || span.innerText;
        if (!txtValue)
            continue;
        if (txtValue.toUpperCase().indexOf(lv_sys_type) > -1) {
            if (!gv_filter) {
                div[i].style.display = "";
                make_all_rows_visible(table, true);
                continue;
            } else {
                if (is_data_exists_in_table(table))
                    div[i].style.display = "";
                else
                    div[i].style.display = "none";
            }
        }
        else {
            // if (!gv_filter) {
            div[i].style.display = "none";
            make_all_rows_visible(table, false);
            // } else {
            //     if (is_data_exists_in_table(table))
            //         div[i].style.display = "";
            //     else
            //         div[i].style.display = "none";
            // }
        }
    }

}