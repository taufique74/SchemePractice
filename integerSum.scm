;sum of integer

(define (sum-integer a b) (
                          if (> a b) 
                          0
                          (+ a (sum-values (+ a 1) b))
                         )
  )

(display (sum-integer 1 3))
