# cv-final-project
### Computer Vision course project repo

### Introduction
I've got an image classification problem related to scans of 4th and 5th grade student work on 16 different math problems. Grad students coded a subset of these, and I'd like the rest categorized in the same way.  All the data is images of digitized 4th and 5th grade student work. Each student answered 8 questions on a 15 minute quiz. The quiz was different for each grade. The labeled data come from students in 19 classrooms (9 Grade 4 and 10 Grade 5). My research team categorized each response image using a variety of codes (ex1., correct and incorrect; ex.2: uses drawings, uses equations, uses written explanation, blank/no explanation.) There are ~3300 labeled images. 

The unlabeled data comes from an administration of the same 15 minute quiz to students in 122 4th and 5th grade classrooms. There are ~14,000 unlabeled responses. The unlabeled responses were digitized as a single PDF for each classroom. Within the PDF, each student's work takes up 2 consecutive pages. There are 4 responses on each page. The student ID is written on the second page (but not the first). 

### Problem Statement
Task 1. Please make a new folder named "images" within the unlabeled data folder to hold the images you extract from the PDFs. The filenames for these images should be 7 digits with two underscore separators: ####\_##\_# where the first 4 digits are the four digits of the PDF filename, the second set of 2 digits are the two digit student ID and the final digit is the question number. Note the question should be renumbered from the PDF to match with the training data, so 2 --> 1, 3 --> 2, 4 --> 3, etc.).

Note that the training images usually do not include the question, so cropping the unlabeled data to exclude the question text might be prudent.

Task 2. Classify the unlabeled images into 5 categories: blank (code C1), illegible/indeterminate (C2 & C3), no justification (either A1 or B1), drawn justification (either A2 or B2), and written justification (either A3 or B3).

Task 3. Classify the no justification, drawn justification, and written justification images into two categories: correct (A codes) or incorrect (B codes).

we use tesseract package for ocr text recognition, following are links to the website
https://tesseract-ocr.github.io/tessdoc/Compiling.html#windows
https://github.com/Microsoft/vcpkg/blob/master/README.md#quick-start-windows
