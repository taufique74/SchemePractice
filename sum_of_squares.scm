;sum of squares with non-tail recursion

(define (sum-of-squares a b) (
                              if (> a b) 0
                              (+ (* a a) (sum-of-squares (+ a 1) b))
                              )
  )

(display (sum-of-squares 1 3))
