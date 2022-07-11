#!/bin/bash
for i in 0.8 0.85 0.9 0.95 1.0 1.05 1.1 1.15 1.2
do
	#let t=0.5*$i r=0.25*$i
	t=$(echo "0.5*$i" | bc)
	r=$(echo "0.25*$i" | bc)
	cat > si2_$i.strc << !
!STRUCTURE
  !GENERIC LUNIT=1.889726124 !END
  !KPOINTS DIV=1 1 1 !END
  !OCCUPATIONS EMPTY=5 NSPIN=1  !END
  !LATTICE T= 0.00000  $t  $t
              $t  0.00000  $t
              $t  $t  0.00000 !END
  !SPECIES NAME= 'Si' ZV=4. M=5.  NPRO= 2 0 0  lrhox=2 ID='SI_.75_6.0'
  !END
  !ATOM   NAME= 'Si_1'  R= 0.00  0.00 0.00 !END
  !ATOM   NAME= 'Si_2'  R= $r  $r $r !END
!END
!EOB	
!
done
