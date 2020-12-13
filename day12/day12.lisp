;;;; Advent of Code Day 12: Rain Risk Solution

(defconstant direction-values
  '((E . ( 1 0))
	(S . (0 -1))
	(W . (-1 0))
	(N . (0  1)))
  "The directions where the ship can go and its quantities")



;;;; Helper functions
(defun input-to-action-list (x)
  "Convert X into a list suitable for parsing."
  (list (subseq x 0 1) (parse-integer (subseq x 1))))

(defun get-directional-value (distance direction )
  "Get the directional value from a given DIRECTION multipled by DISTANCE.
    - If the direction is a number, return by index.
    - If the direction is a string, return by association."
  (assert (or (stringp direction)
			  (numberp direction)))
  (map 'list
	   #'(lambda (x) (* x distance))
	   (if (numberp direction)
		   (cdr (nth direction direction-values))
		   (cdr (assoc (intern direction) direction-values)))))

(defun new-ship-position (position offset)
  "Calculate a new position for the ship, simply adding together POSITION and OFFSET."
  (mapcar #'+ position offset))



;;;; Part 1 Solution
(defun aoc-2020-day-12-part-1 (input)
  "Solve part 1 with given INPUT."
  (let ((ship-position '(0 0))
		(ship-direction 0))
	(loop for (action param) in (map 'list #'input-to-action-list input)
		  do (cond 
			   ;; move the ship forward based on the direction
			   ((string= "F" action)
				(setf ship-position (new-ship-position
									 ship-position
									 (get-directional-value param ship-direction))))
			   ;; rotate the ship clockwise
			   ((string= "R" action)
				(setf ship-direction (mod (+ ship-direction (floor param 90)) 4)))
			   ;; rotate the ship counter-clockwise
			   ((string= "L" action)
				(setf ship-direction (mod (- ship-direction (floor param 90)) 4)))
			   ;; move the ship based on given direction
			   (t
				(setf ship-position (new-ship-position
									 ship-position
									 (get-directional-value param action))))))
	(reduce #'+ (map 'list #'abs ship-position))))



;;;; Part 2 Solution
(defun aoc-2020-day-12-part-2 (input)
  "Solve part 2 with given INPUT."
  (defun waypoint-position-manipulate (position direction)
	"Manipulate the POSITION of the waypoint depending on the
    DIRECTION in relation to the ship"
	(assert (and (>= direction 0)
				 (< direction 4)))
	(let ((x (first position))
		  (y (second position)))
	  (cond ((= 0 direction) (list x y))
			((= 1 direction) (list y (- x)))
			((= 2 direction) (list (- x) (- y)))
			((= 3 direction) (list (- y) x)))))
  (let ((waypoint-position '(10 1))
		(ship-position '(0 0)))
	(loop for (action param) in (map 'list #'input-to-action-list input)
		  do (cond 
			   ;; move the ship forward based on the waypoint's position
			   ;; and direction
			   ((string= "F" action)
				(setf ship-position
					  (mapcar #'+
							  (map 'list
								   #'(lambda (x) (* x param))
								   waypoint-position)
							  ship-position)))
			   ;; rotate the waypoint clockwise
			   ((string= "R" action)
				(setf waypoint-position (waypoint-position-manipulate
										 waypoint-position
										 (mod (floor param 90) 4))))
			   ;; rotate the waypoint counter-clockwise
			   ((string= "L" action)
				(setf waypoint-position (waypoint-position-manipulate
										 waypoint-position
										 (mod (- (floor param 90)) 4))))
			   ;; move the waypoint based on given direction
			   (t
				(setf waypoint-position (new-ship-position
										 waypoint-position
										 (get-directional-value param action))))))
	(reduce #'+ (map 'list #'abs ship-position))))



;;;; Testing
(let ((input (with-open-file (stream "input.txt")
			   (loop for line = (read-line stream nil)
					 while line
					 collect line))))
  (print (aoc-2020-day-12-part-1 input))
  (print (aoc-2020-day-12-part-2 input)))
