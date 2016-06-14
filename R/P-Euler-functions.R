# Project Euler functions

# Generate a list of primes up to a certain size
    primegen<-function(limit){
        
        instance<-2
        primes<-instance
        instance<-instance+1
        primes<-c(primes,instance)
        
        while (instance < limit){
            instance<- instance + 2
            test<-T
            sqrt_inst<-sqrt(instance)
            for(a in primes){
                if(a > sqrt_inst) break
                if(instance%%a==0){
                    test<-F
                    break
                }
            }
            if(test){
                primes<-c(primes,instance)
            }
        }
        
        primes
    }

# Clean_all program
    cl.all<-function(){    
        rm(list=ls())
        gc()
    }