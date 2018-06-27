


For First part of the assignment (transform.py, transformed.csv):

1. I read the wikipedia page and parsed it through BeautifulSoup.

2. Searched for all the tables and took the required table as 'table'

3. Searched for the first row in the table, stored the 'th' into a list and appended the list into 'data'(final extracted list)

4. For all the rest of rows, performed the following action:
	a. Parsed all the columns of each row until the date the matches took place.
	b. For each column, extracted the data according to the requirement.
	c. Appended the data of a single row into a list 'lst'
	d. Appended the 'lst' to 'data'

5. Created a csv file 'transformed.csv' and wrote 'data' to it.


For second part of the assignment:

(clean.py, cleaned.txt)

1. Read the file from command line

2. Some courses had "-" in their name. Replaced "-" with " " so that while splitting the prof-courses by ("-"), course names are not sliced.

3. For all the format of professor names, changed it to last_name, first_name.

4. Defined the functions for calculating jaccard distance.

5. For all the similar courses but slight error in their names, implemented the jaccard function, and replaced the ones with high jaccard distance with one of arbitrarily chosen course name to achieve results close to optimal results.

6. For all the professors, searched for similar professors having character jacquard distance greater than 0.8 and grouped their courses using a dictionary.

7. Sorted the courses for each professor.

8. Stored the dictionary into a list.

9. Sorted the list according to last names of professors.

10. Converted the list into the same format as original.

11. Created a txt file 'cleaned.txt' and stored the data into the file.


(query.py)

1. Read the file from command line.

2. For Q1, Traversed through the name of professors and added them to dictionary with key : prof name and value: count. Dict stores unique values. Counted the keys which is number of courses.

3. For Q2, Read the prof from command line, split the list by prof and courses. Traversed through each prof name and when the name matches the prof whose courses are needed, print the courses corresponding to that professor.

4. For Q3, For all the courses, stored the professors with at least 5 courses into a dictionary. Calculated the jacquard distance for them and printed the professors with highest jacquard distance.