/Responsive Calculator Webpage

This project is a simple, responsive calculator built using HTML, CSS, and JavaScript. It performs basic arithmetic operations and works seamlessly on both desktop and mobile devices.


/Features
Supports addition (+), subtraction (-), multiplication (*), and division (/) 
Handles decimal inputs  
Clear (C) button to reset the screen  
Prevents multiple operators or trailing decimals  
Handles divide-by-zero errors gracefully  
Keyboard input support (e.g., press "1" on your keyboard)  
Theme toggle (Light/Dark mode) with a button  

/Interface Preview

\[ Calculator Interface ]
\[  7  8  9  / ]
\[  4  5  6  \* ]
\[  1  2  3  - ]
\[  .  0  =  + ]
\[   C        ]

/How to Run the Project

 No installation or server required. Just open the HTML file in a browser.

/Steps:
1. Download or clone this repository.
2. Open the `calculator/index.html` file in any modern web browser.
3. Start calculating

/Sample Input and Output

 Input              Output     

 `12 + 4` then `=`   `16`       
 `15 / 3` then `=`   `5`        
 `7 * 0` then  `=`    `0`        
 `5 / 0` then  `=`   `Error`    
`.` then `.`         Prevents double decimal 

---

/Assumptions

- Arithmetic follows left-to-right evaluation (not full operator precedence).
- Inputs are typed via buttons or keyboard.
- Only one decimal point is allowed per number.
- The `=` key computes and updates the display.

/Features Implemented

-Theme toggle with sun emoji 
- Keyboard input
