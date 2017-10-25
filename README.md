# Berkeley-courses-finder
This is a web spider (web crawler) based on the Berkeley Academic Guide. It will return courses that related to the keyword.

Users first choose a subject through the academic guide, then copy the link to HOMEPAGE in main.py file. For example, the HOMEPAGE in the file now is 'search results for computer science'.

Then users can type in arbitrary keyword, any course that 1. either contains the keyword in its title 2. or contains the keyword in its description will be stored in courses.txt, a new file created by the program in the same directory.

When a Berkeley student is planning their future courses, there is a lot of redundant information in Berkeley Academic Guide. Every sessions (including discussions and labs) are shown, which make the page way too long for students to dig useful information. The crawler, in contrast, only display the course names (like COMPSCI 61A) and no same names will be included.

The number of threads initially used is 8. Feel free to change it according to your own CPU capacitance and operating system.
