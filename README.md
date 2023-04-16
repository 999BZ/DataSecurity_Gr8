# DataSecurity_Gr8
Four Square Cipher

Këtë algoritëm e kemi punuar me gjuhën programuese Python.
Four Square Cipher është një algoritëm simetrik i enkriptimit i krijuar nga Felix Delastelle. Punon me katër matrica (5x5) të mbushura me alfabetin e gjuhës angleze, 
pasi që maksimumi i shkronjave që mund të zënë vend në këtë lloj matrice është 25 atëherë një shkronjë duhet të largohet, preferohet largimi i shkronjës J pasi që nga 
statistika e përdorimit të shkronjave në gjuhën angleze kjo shkronjë përdoret më së paku. Ne e kemi bërë variabile largimin e shkronjës sipas dëshirës së përdoruesit.
Krijimin e katër matricave e kemi bërë përmes klasës Matrix të krijuar nga ne ku çdo herë që e krijojmë një objekt të ri të kësaj klase krijohet një set i ri i matricave.
Matricat UL(Up Left) dhe DR(Down Right) kanë vetëm përmbajtjen e alfabetit kurse matricat UR(Up Right) dhe DL(Down Left) në fillim kanë dy çelësa(gjithashtu variabile)
pastaj vazhdohet alfabeti duke mos i përsëritur shkronjat që gjenden në çelësa. Tek çelësat shkronjat nuk duhet përsëritur.

Enkriptimi bëhet përmes funksionit Encrypt i cili ka dy parametra: setin e matricave dhe mesazhin. Në një iterim enkriptohen dy shkronja, shkronja e parë kërkohet tek 
matrica UL kurse e dyta tek DR, pastaj krijohet një drejtkëndësh me skaje në këto dy shkronja. Në dy skajet tjera gjenden shkronjat e enkriptuara me renditje UR, DL, 
procesi vazhdon për të gjitha shkronjat e nëse numri i tyre është tek atëherë shtohet një X në fund. Meqenëse ky algoritëm është simetrik procesi i dekriptimit është 
proces revers i enkriptimit që kryhet përmes funksionit Decrypt.

Libraritë e përdorura: 
import string - për manipulim me stringje,
from more_itertools import unique_everseen - për shmangien e përsëritjes së shkronjave në çelësa,
import numpy as np - për krijimin e matricës 

Anëtarët: Arnis Hoxha, Astrit Krasniqi, Besmira Berisha, Blendi Zeqiri

