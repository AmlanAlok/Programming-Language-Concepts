// AMAZING
//
// Converted from BASIC to Javascript by Oscar Toledo G. (nanochess)
//
// function print(str)
// {
//     document.getElementById("output").appendChild(document.createTextNode(str));
// }


function input()
{
    var input_element;
    var input_str;

    return new Promise(function (resolve) {
                       input_element = document.createElement("INPUT");

                       console.log("? ");
                       input_element.setAttribute("type", "text");
                       input_element.setAttribute("length", "50");
                       document.getElementById("output").appendChild(input_element);
                       input_element.focus();
                       input_str = undefined;
                       input_element.addEventListener("keydown", function (event) {
                                                      if (event.keyCode == 13) {
                                                      input_str = input_element.value;
                                                      document.getElementById("output").removeChild(input_element);
                                                      console.log(input_str);
                                                      console.log("\n");
                                                      resolve(input_str);
                                                      }
                                                      });
                       });
}

function tab(space)
{
    var str = "";
    while (space-- > 0)
        str += " ";
    return str;
}

console.log(tab(28) + "AMAZING PROGRAM\n");
console.log(tab(15) + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n");
console.log("\n");
console.log("\n");
console.log("\n");
console.log("FOR EXAMPLE TYPE 10,10 AND PRESS ENTER\n");
console.log("\n");

// Main program
async function main()
{
    while (1) {
        console.log("WHAT ARE YOUR WIDTH AND LENGTH");
        // a = await input();
        // h = parseInt(a);
        // v2 = parseInt(a.substr(a.indexOf(",") + 1));
        h = 10
        v2 = 10
        if (h > 1 && v2 > 1)
            break;
        console.log("MEANINGLESS DIMENSIONS.  TRY AGAIN.\n");
    }
    w = [];
    v = [];
    for (i = 1; i <= h; i++) {
        w[i] = [];
        v[i] = [];
        for (j = 1; j <= v2; j++) {
            w[i][j] = 0;
            v[i][j] = 0;
        }
    }
    console.log("\n");
    console.log("\n");
    console.log("\n");
    console.log("\n");
    q = 0;
    z = 0;
    x = Math.floor(Math.random() * h + 1);
    polo = ""
    for (i = 1; i <= h; i++) {
        if (i == x)
            // console.log(".  ");
            polo = polo + ".  "
        else
            // console.log(".--");
            // polo.push(".--")
            polo = polo + ".--"
    }
    // console.log(".\n");
    // polo.push(".\n")
    polo = polo + ".\n"
    console.log(polo);
    c = 1;
    w[x][1] = c;
    c++;
    r = x;
    s = 1;
    entry = 0;
    while (1) {
        if (entry == 2) {	// Search for a non-explored cell
            do {
                if (r < h) {
                    r++;
                } else if (s < v2) {
                    r = 1;
                    s++;
                } else {
                    r = 1;
                    s = 1;
                }
            } while (w[r][s] == 0) ;
        }
        if (entry == 0 && r - 1 > 0 && w[r - 1][s] == 0) {	// Can go left?
            if (s - 1 > 0 && w[r][s - 1] == 0) {	// Can go up?
                if (r < h && w[r + 1][s] == 0) {	// Can go right?
                    // Choose left/up/right
                    x = Math.floor(Math.random() * 3 + 1);
                } else if (s < v2) {
                    if (w[r][s + 1] == 0) {	// Can go down?
                        // Choose left/up/down
                        x = Math.floor(Math.random() * 3 + 1);
                        if (x == 3)
                            x = 4;
                    } else {
                        x = Math.floor(Math.random() * 2 + 1);
                    }
                } else if (z == 1) {
                    x = Math.floor(Math.random() * 2 + 1);
                } else {
                    q = 1;
                    x = Math.floor(Math.random() * 3 + 1);
                    if (x == 3)
                        x = 4;
                }
            } else if (r < h && w[r + 1][s] == 0) {	// Can go right?
                if (s < v2) {
                    if (w[r][s + 1] == 0) {	// Can go down?
                        // Choose left/right/down
                        x = Math.floor(Math.random() * 3 + 1);
                    } else {
                        x = Math.floor(Math.random() * 2 + 1);
                    }
                    if (x >= 2)
                        x++;
                } else if (z == 1) {
                    x = Math.floor(Math.random() * 2 + 1);
                    if (x >= 2)
                        x++;
                } else {
                    q = 1;
                    x = Math.floor(Math.random() * 3 + 1);
                    if (x >= 2)
                        x++;
                }
            } else if (s < v2) {
                if (w[r][s + 1] == 0) {	// Can go down?
                    // Choose left/down
                    x = Math.floor(Math.random() * 2 + 1);
                    if (x == 2)
                        x = 4;
                } else {
                    x = 1;
                }
            } else if (z == 1) {
                x = 1;
            } else {
                q = 1;
                x = Math.floor(Math.random() * 2 + 1);
                if (x == 2)
                    x = 4;
            }
        } else if (s - 1 > 0 && w[r][s - 1] == 0) {	// Can go up?
            if (r < h && w[r + 1][s] == 0) {
                if (s < v2) {
                    if (w[r][s + 1] == 0)
                        x = Math.floor(Math.random() * 3 + 2);
                    else
                        x = Math.floor(Math.random() * 2 + 2);
                } else if (z == 1) {
                    x = Math.floor(Math.random() * 2 + 2);
                } else {
                    q = 1;
                    x = Math.floor(Math.random() * 3 + 2);
                }
            } else if (s < v2) {
                if (w[r][s + 1] == 0) {
                    x = Math.floor(Math.random() * 2 + 2);
                    if (x == 3)
                        x = 4;
                } else {
                    x = 2;
                }
            } else if (z == 1) {
                x = 2;
            } else {
                q = 1;
                x = Math.floor(Math.random() * 2 + 2);
                if (x == 3)
                    x = 4;
            }
        } else if (r < h && w[r + 1][s] == 0) {	// Can go right?
            if (s < v2) {
                if (w[r][s + 1] == 0)
                    x = Math.floor(Math.random() * 2 + 3);
                else
                    x = 3;
            } else if (z == 1) {
                x = 3;
            } else {
                q = 1;
                x = Math.floor(Math.random() * 2 + 3);
            }
        } else if (s < v2) {
            if (w[r][s + 1] == 0) 	// Can go down?
                x = 4;
            else {
                entry = 2;	// Blocked!
                continue;
            }
        } else if (z == 1) {
            entry = 2;	// Blocked!
            continue;
        } else {
            q = 1;
            x = 4;
        }
        if (x == 1) {	// Left
            w[r - 1][s] = c;
            c++;
            v[r - 1][s] = 2;
            r--;
            if (c == h * v2 + 1)
                break;
            q = 0;
            entry = 0;
        } else if (x == 2) {	// Up
            w[r][s - 1] = c;
            c++;
            v[r][s - 1] = 1;
            s--;
            if (c == h * v2 + 1)
                break;
            q = 0;
            entry = 0;
        } else if (x == 3) {	// Right
            w[r + 1][s] = c;
            c++;
            if (v[r][s] == 0)
                v[r][s] = 2;
            else
                v[r][s] = 3;
            r++;
            if (c == h * v2 + 1)
                break;
            entry = 1;
        } else if (x == 4) {	// Down
            if (q != 1) {	// Only if not blocked
                w[r][s + 1] = c;
                c++;
                if (v[r][s] == 0)
                    v[r][s] = 1;
                else
                    v[r][s] = 3;
                s++;
                if (c == h * v2 + 1)
                    break;
                entry = 0;
            } else {
                z = 1;
                if (v[r][s] == 0) {
                    v[r][s] = 1;
                    q = 0;
                    r = 1;
                    s = 1;
                    while (w[r][s] == 0) {
                        if (r < h) {
                            r++;
                        } else if (s < v2) {
                            r = 1;
                            s++;
                        } else {
                            r = 1;
                            s = 1;
                        }
                    }
                    entry = 0;
                } else {
                    v[r][s] = 3;
                    q = 0;
                    entry = 2;
                }
            }
        }
    }
    for (j = 1; j <= v2; j++) {
        str = "I";
        for (i = 1; i <= h; i++) {
            if (v[i][j] < 2)
                str += "  I";
            else
                str += "   ";
        }
        console.log(str + "\n");
        str = "";
        for (i = 1; i <= h; i++) {
            if (v[i][j] == 0 || v[i][j] == 2)
                str += ":--";
            else
                str += ":  ";
        }
        console.log(str + ".\n");
    }
// If you want to see the order of visited cells
//    for (j = 1; j <= v2; j++) {
//        str = "I";
//        for (i = 1; i <= h; i++) {
//            str += w[i][j] + " ";
//        }
//        console.log(str + "\n");
//    }
}

main();
