# Debugging
## 16.08.2021
**Selfconsistency Loop not converged**

>    - w.r.t. GRHOT2 it is apparently not converged. Changing eclsda1 value and seeing the effect of that on DEXC1(3): 
>        - -0.92E-04 (eclsda1=-0.05)
>        - Changing to eclsda1=-0.000005 and 0.00005 for the derivatives finished the SETUP CONSTRUCTION. → Now it stops in ATOMS_INITIALIZE
>    - Solved the Self-Consistency Loop problem, now the ATOMS_INITIALIZE:
>        - Try switching to DFT_META and see what's up.

## 31.08.2021
>    - DFT_META() seems to be called now. → Testing on H2 to see if the bond length is any good.
>    - Without the mixed terms I get a bond length of d(H2)=1.204A
>    - **Idea:** Create smaller/copy routines of scan_u() for first, second and third derivatives.

## 06.09.2021
>    TSPIN is set to F in DFT_META()→ RHOS=0 because of it

## 21.09.2021
>    - Run for a few steps and then go for START=F. Seems to be going in the right direction
>    - → do it for H2O tomorrow
>    - Code runs for H2 → wrong bond length (1.14A instead of 0.74A)
>        
>        →add the mixed terms to see if that will improve it.

## 11.11.2021
>    - I put D2EXC(:,:)=0 and D3EXC(:,:,:)=0 into the SCAN$EVAL3 routine to let it print out the results of the scna_u3 calculation for that test case.
>    - → add the mixed terms and the additional transformations
>        - Mixed alpha terms (done)

## 15.11.2021
>    - I put in all mixed terms (done)
>    - I set D2EXC(1:7,1:7)=10.0d0 before and after the print statement for the D2EXC to see whether D2EXC can be affected outside and will be put in anew for the next iteration → it does.
>    - **I notice that in the pdf I didn't put in what is needed when it comes to the mixed terms for the third derivatives (only the second ones).**
>    - I don't define the mixed terms of D2EXC and D3EXC, but instead the mixed terms according to my derivatives that are put into the non-mixed terms by Peter's definition.

## 16.11.2021
> - I put the mixed terms into their designated places for the second and third derivatives (according to my variable definition)

## 19.11.2021
> Do the convergence without auto

## 23.11.2021
> - I added eclsda1 by Chachiyo 2016 including the derivatives. (currently NSTEP=10 done until 3.6 → continue with 3.7) DONE

## 26.11.2021
> - After doing the figure for H2, do an atom relaxation calculation to see if it hits the minimum of the static calculations.
>    - Doing it in kernelrun/

---
---
# Mixed Terms

- I did the mixed derivatives of $\zeta$ and should be able to take the next derivatives simply by exchanging the non-mixed $\zeta$ derivatives with the corresponding mixed ones.

Done so far:

- mixed terms are in the code
- All derivatives have been updated with the mixed terms.


# H2
H1 scf energy: -0.3662252H = -0.7324504Ry
H2:

| Bond Length [Bohr] | Energy [H] | Energy [Ry] |
| -------------------|------------|-------------|
| 2.1883026948       |-0.5804253  |-1.1608506   |

# S22 as reference data
## SCAN in kcal/mol
|System|Result        |Reference|Result-Reference|
|------|--------------|---------|----------------|
|1     |41.5869443    |3.17     |38.4169443      |
|2     |13.09436849   |5.02     |8.07436849      |
|3     |190.1483379   |18.8     |171.3483379     |
|4     |-53.005422836 |16.12    |-69.12542284    |
|5     |-3930.1411816 |20.69    |3950.831182     |
|6     |-8108.28470243|17       |8125.284702     |
|7     |-18089.1043854|16.74    |18105.84439     |
|8     |18.69470349   |0.53     |18.16470349     |
|9     |7.312432213   |1.5      |5.812432213     |
|10    |16.88760132   |1.45     |15.43760132     |
|11    |8.898462748   |2.62     |6.278462748     |
|12    |6.072096722   |4.2      |1.872096722     |
|13    |-42.194875561 |9.74     |51.93487556     |
|14    |-6.8898044923 |4.59     |-11.47980449    |
|15    |-182.69308453 |11.66    |-194.3530845    |
|16    |18.17719632   |1.51     |16.66719632     |
|17    |14.47394837   |3.29     |11.18394837     |
|18    |12.80897712   |2.32     |10.48897712     |
|19    |26.06888265   |4.55     |21.51888265     |
|20    |4.98619135    |2.71     |2.27619135      |
|21    |-1919.6686705 |5.62     |-1925.288671    |
|22    |-477.44401107 |7.09     |484.5340111     |

- not enough space on office PC. Try doing it on the external drive.
- → that worked

## 3.12.2021
- Reducing DT=0.01/0.02. That seems to have solved the issues about the wave function mass errors.

- S22 links: [S22 database1](http://www.thch.uni-bonn.de/tc.old/downloads/GMTKN/GMTKN24/S22ref.html) [S22 database2](http://www.thch.uni-bonn.de/tc.old/downloads/GMTKN/GMTKN30/S22ref.html)

## 6.12.2021
- Doing the MB08 data set: [MB08 dataset](http://www.thch.uni-bonn.de/tc.old/downloads/GMTKN/GMTKN30/MB08-165ref.html)

## 7.12.2021
- Continuing the calculation for the MB08 data set. (Finished until 080 so far).

## 8.12.2021
- Continuing the calculation for the MB08 data set. (Finished until 150 so far).

## 16.12.2021
- I realized that there was some error with [strc.py](http://strc.py) → redo S22 and MB08 after isol22.
- ISOL22: 20 steps done. → next: NSTEP=100 START=F

## 17.12.2021
- S22: NSTEP=150 START=F (done)
- MB08: NSTEP=150 START=F (done)
- ISOL22: NSTEP=150 START=F (done)

## 23.12.2021
- Finished PBE runs on S22, MB08 and ISOL22: seems to be even worse when compared to experimental results. →continue with MINFRIC=0.01 to converge better and compare again.

## 18.01.2022 
- PBE calculations on s22, isol22, mb08 are done. → SCAN seems to perform better on average. 