; calculates factorial using non-tail recursion

(define (factorial n)
            (if (= n 0) 
                1
            (* n (factorial(- n 1)))  )
)

(display (factorial 5))