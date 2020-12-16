;;;; Advent of Code 2020 Day 14 Solution

(load "~/quicklisp/setup.lisp")
(ql:quickload :cl-ppcre)
(ql:quickload :str)
(ql:quickload :alexandria)



;;;; Solution for Part 1
(defun aoc-2020-day14-part-1 (input)
  "Solve Day 14 - Part 1 with provided INPUT."
  (alexandria:hash-table-values
   (let ((mask "")
		 (mem (make-hash-table)))
	 (loop :for (cmd param) in input
		   :if (string= cmd "mask")
			 :do (setf mask param)
		   :else
			 :do (setf (gethash (intern (string (ppcre:register-groups-bind (index)
													("mem[(\\d+)]" cmd)
												  index)))
								mem)
					   (parse-integer
						(concatenate
						 'string
						 (let ((num (format nil
											(concatenate 'string
														 "~"
														 (write-to-string (length mask))
														 ",'0b")
											(parse-integer param))))
						   (loop :for i below (length num)
								 :if (char= (char mask i) #\X)
								   :collect (char num i)
								 :else
								   :collect (char mask i))))
						:radix 2)))
	 mem)))



;;;; Solution for Part 2





;;;; Testing
(let ((input (with-open-file (stream "test.txt")
			   (loop for line = (read-line stream nil)
					 while line
					 collect (map 'list
								  #'str:trim
								  (cl-ppcre:split " = " line))))))
  (print input)
  (print (aoc-2020-day14-part-1 input)))
