if (
    user.length == 12 
    && (user[0] == "b")                                         // "b"
    && (user.charCodeAt(0) == user.charCodeAt(1) - 19)          // "u"
    && (String.fromCharCode(user.charCodeAt(3) & 0x7F) == "n")  // "n"
    && (user[3] == user[2])                                     // "n"
    && (user.charCodeAt(4) == user.charCodeAt(1) + user[7] * 1) // "y"
    && (user[5] == "X!&)="[0])                                  // "X"
    && (user[6] == String.fromCharCode(109))                    // "m"
    && (user[7] == (1 << 2))                                    // "4"
    && (user[8] == "s")                                         // "s"
    && (user.charCodeAt(8) == user.charCodeAt(9) - 1)           // "t"
    && (user[10] == user[7] - 1)                                // "3"
    && (user[11] == String.fromCharCode(114)))                  // "r"

var user = "bunnyXm4st3r"

if (pass == magic(user))
// magic("bunnyXm4st3r") === "cvoozYs4ut5n"
pass = "cvoozYs4ut5n";
