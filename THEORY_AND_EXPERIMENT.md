# Fonament teòric i relacions experimentals

> Transcripció del contingut tècnic central de l'informe *Filtratge espacial en un sistema 4f*. S'ha reformatat en Markdown i LaTeX per facilitar-ne la lectura a GitHub; les equacions i integrals es mantenen completes. El document canònic és [`report/Fourier_Optics_4f_Report.pdf`](report/Fourier_Optics_4f_Report.pdf).

## 2.1 Funció de transmissió i freqüències espacials

El pla objecte $P_0$ conté un element que modifica el camp incident segons la posició transversal. L'objecte pot ser una escletxa, una xarxa periòdica, una retícula o una transparència amb un patró imprès, entre d'altres. Sigui $(x_0,y_0)\in P_0$ i $U_i(x_0,y_0)$ el camp incident sobre $P_0$. Aleshores, el camp immediatament posterior a l'objecte és

$$
U_0(x_0,y_0)=t(x_0,y_0)U_i(x_0,y_0). \tag{1}
$$

on $t(x,y)$ és la funció de transmissió en amplitud de l'objecte. En una zona transparent es té $t(x_0,y_0)\simeq 1$, mentre que en una zona opaca es té $t(x_0,y_0)\simeq 0$. En general, si l'objecte també introdueix un retard de fase $\phi(x,y)$, la funció de transmissió pot ser complexa i es pot escriure com

$$
t(x_0,y_0)=|t(x_0,y_0)|e^{i\phi(x_0,y_0)}. \tag{2}
$$

No obstant, en aquesta pràctica es consideren principalment objectes d'amplitud, és a dir, que modifiquen la quantitat de llum transmesa segons la posició, com escletxes, xarxes o transparències impreses. Per tant, la informació rellevant queda associada sobretot a la variació espacial del mòdul de la funció de transmissió, $|t(x_0,y_0)|$.

La funció de transmissió descriu l'objecte en l'espai real. Tanmateix, també es pot descriure en termes dels seus components espacials mitjançant la transformada de Fourier. En el cas general de dues dimensions, es té

$$
T(\nu_x,\nu_y)=\iint_{\mathbb{R}^2} t(x_0,y_0)e^{-i2\pi(\nu_xx_0+\nu_yy_0)}\,dx_0\,dy_0. \tag{3}
$$

on les variables $\nu_x$ i $\nu_y$ són freqüències espacials i tenen dimensions d'invers de la longitud. Per exemple, es poden expressar en $\mathrm{mm}^{-1}$, la qual cosa correspondria al nombre de franges per mil·límetre en el cas d'una xarxa en la direcció en qüestió.

No obstant, la funció de transmissió d'alguns objectes utilitzats al laboratori presenta variació apreciable només en una direcció transversal. Per exemple, una escletxa vertical o una xarxa de franges verticals presenten variació en la direcció $x_0$, però són aproximadament invariants en la direcció $y_0$. En aquest cas es pot escriure $t(x_0,y_0)=t(x_0)$ i la descripció freqüencial es redueix a una transformada de Fourier unidimensional,

$$
T(\nu_x)=\int_{\mathbb{R}} t(x_0)e^{-i2\pi\nu_xx_0}\,dx_0. \tag{4}
$$

La interpretació de les freqüències espacials depèn de la forma concreta de la funció de transmissió $t(x_0,y_0)$. En general, les variacions que tenen lloc al llarg de distàncies majors s'associen a freqüències espacials menors, mentre que les variacions que tenen lloc en distàncies menors s'associen a freqüències espacials majors.

## 2.2 Difracció de Fresnel i Fraunhofer

La difracció descriu la redistribució del camp lluminós quan una ona troba un obstacle, una obertura o un element que en modifica la propagació. El patró observat depèn de la geometria del muntatge, de la longitud d'ona i de la distància entre l'objecte difractiu i el pla d'observació. En el règim de Fresnel, el pla d'observació es troba a una distància finita i la curvatura dels fronts d'ona no és negligible, de manera que el patró depèn de manera apreciable de la distància de propagació. En canvi, en el règim de Fraunhofer, el pla d'observació és prou allunyat perquè el patró es pugui interpretar com una distribució angular dels components difractats.

Un criteri habitual per estimar la validesa del règim de Fraunhofer és mitjançant el nombre de Fresnel $N_F:=a^2/(\lambda z)$, on $a$ és una mida transversal característica de l'obertura o de l'objecte, $\lambda$ és la longitud d'ona i $z$ és la distància entre el pla de l'objecte difractiu i el pla d'observació. El règim de Fraunhofer correspon, aproximadament, a $N_F\ll 1$, és a dir, $z\gg a^2/\lambda$.

La importància del règim de Fraunhofer és que el camp difractat es relaciona directament amb el contingut freqüencial de l'objecte. Si l'objecte és il·luminat per una ona plana i el camp immediatament posterior és $U_0(x_0,y_0)$, el camp observat en el règim de Fraunhofer és proporcional a la transformada de Fourier espacial de $U_0$.

## 2.3 Pla focal d'una lent i pla de Fourier

En propagació lliure, el règim de Fraunhofer s'assoleix quan el pla d'observació és prou allunyat de l'objecte. Tanmateix, una lent convergent permet obtenir la mateixa informació a una distància finita. En efecte, si l'objecte se situa al pla focal anterior d'una lent prima de distància focal $f$, el camp format al pla focal posterior és proporcional a la transformada de Fourier espacial del camp immediatament posterior a l'objecte.

Un component del camp que surt de l'objecte amb inclinacions petites $\theta_x$ i $\theta_y$, projectades respectivament sobre els plans $x_0z$ i $y_0z$, queda focalitzat en una posició $(x_1,y_1)$ del pla focal posterior. En el model de lents primes, es té

$$
x_1=f\tan\theta_x\simeq f\sin\theta_x,\qquad y_1=f\tan\theta_y\simeq f\sin\theta_y. \tag{5}
$$

A partir de l'Eq. (3), es defineix la transformada inversa

$$
t(x_0,y_0)=\iint_{\mathbb{R}^2}T(\nu_x,\nu_y)e^{i2\pi(\nu_xx_0+\nu_yy_0)}\,d\nu_x\,d\nu_y. \tag{6}
$$

En comparar la descomposició de Fourier amb una ona plana monocromàtica, s'obté

$$
\nu_x=\frac{\sin\theta_x}{\lambda},\qquad \nu_y=\frac{\sin\theta_y}{\lambda}. \tag{7}
$$

Seguidament, es combina l'Eq. (5) amb l'Eq. (7) i s'obté la correspondència entre les coordenades físiques del pla focal posterior i les freqüències espacials

$$
\nu_x\simeq\frac{x_1}{\lambda f},\qquad \nu_y\simeq\frac{y_1}{\lambda f}. \tag{8}
$$

Per expressar aquesta propietat de manera compacta, si $U_0(x_0,y_0)$ és el camp immediatament posterior a l'objecte, se'n defineix la transformada de Fourier espacial com

$$
\mathcal{F}\{U_0\}(\nu_x,\nu_y):=\iint_{\mathbb{R}^2}U_0(x_0,y_0)e^{-i2\pi(\nu_xx_0+\nu_yy_0)}\,dx_0\,dy_0. \tag{9}
$$

Aleshores, llevat de factors constants i de fase que no modifiquen la distribució d'intensitat, el camp al pla focal posterior de la lent satisfà

$$
U_1(x_1,y_1)\propto \mathcal{F}\{U_0\}\left(\frac{x_1}{\lambda f},\frac{y_1}{\lambda f}\right). \tag{10}
$$

La distribució d'intensitat observada en una pantalla situada al pla focal és proporcional al mòdul quadrat de la transformada,

$$
I_1(x_1,y_1)\propto \left|\mathcal{F}\{U_0\}\left(\frac{x_1}{\lambda f},\frac{y_1}{\lambda f}\right)\right|^2. \tag{11}
$$

## 2.4 Sistema 4f amb il·luminació col·limada

La configuració experimental representada a la Fig. 1 es divideix en una etapa prèvia d'il·luminació i una etapa de filtratge espacial basada en un sistema 4f. La font puntual $S$ se situa al pla focal anterior de la lent $L_0$. En aquestes condicions, la lent $L_0$ transforma el feix procedent de $S$ en un feix coherent i aproximadament col·limat.

El sistema 4f queda definit per $P_0-L_1-P_1-L_2-P_2$. El pla objecte $P_0$ se situa al pla focal anterior de la lent $L_1$, que forma el pla focal posterior $P_1$. El pla $P_1$ correspon al pla de Fourier de l'objecte. La lent $L_2$ se situa a una distància focal del pla $P_1$ i forma la imatge al pla $P_2$.

En general, si les distàncies focals de $L_1$ i $L_2$ no coincideixen, l'augment transversal ve donat per

$$
M=-\frac{f_2}{f_1}. \tag{12}
$$

Si la il·luminació sobre $P_0$ és coherent i aproximadament col·limada, dins de la regió ocupada per l'objecte es pot escriure $U_i(x_0,y_0)\simeq A_0$, on $A_0\in\mathbb{C}$ és una constant complexa que pot incloure una fase global. Aleshores, per l'Eq. (1), el camp immediatament posterior a l'objecte és $U_0(x_0,y_0)\simeq A_0t(x_0,y_0)$. Per tant, segons l'Eq. (10), el camp al pla $P_1$ és proporcional a

$$
U_1(x_1,y_1)\propto A_0\iint_{\mathbb{R}^2} t(x_0,y_0)
\exp\left[-i2\pi\left(\frac{x_1}{\lambda f_1}x_0+\frac{y_1}{\lambda f_1}y_0\right)\right]dx_0\,dy_0. \tag{13}
$$

És a dir,

$$
U_1(x_1,y_1)\propto A_0T\left(\frac{x_1}{\lambda f_1},\frac{y_1}{\lambda f_1}\right). \tag{14}
$$

En canvi, si el feix incident presenta una amplitud transversal no uniforme o una curvatura de fase apreciable, per l'Eq. (1) el camp posterior a l'objecte és $U_0(x_0,y_0)=U_i(x_0,y_0)t(x_0,y_0)$ i, per tant, el camp al pla $P_1$ és proporcional a

$$
U_1(x_1,y_1)\propto \iint_{\mathbb{R}^2}U_i(x_0,y_0)t(x_0,y_0)
\exp\left[-i2\pi\left(\frac{x_1}{\lambda f_1}x_0+\frac{y_1}{\lambda f_1}y_0\right)\right]dx_0\,dy_0. \tag{15}
$$

Així, el pla $P_1$ representaria la transformada del producte $U_i(x_0,y_0)t(x_0,y_0)$ i no només la transformada de la funció de transmissió de l'objecte.

![Esquema original del sistema 4f](assets/figure_1_4f_system.png)

## 2.5 Filtratge espacial

A partir de la identificació del pla $P_1$ com el pla de Fourier del sistema, es pot realitzar filtratge espacial coherent introduint-hi un filtre espacial o màscara de filtratge per modificar selectivament els components freqüencials de l'objecte.

Sigui $H(\nu_x,\nu_y)$ la funció de transferència del filtre situat al pla de Fourier, la qual descriu quins components freqüencials es transmeten, s'atenuen o es bloquegen. Si l'espectre espacial del camp abans del filtre és proporcional a $\mathcal{F}\{U_0\}(\nu_x,\nu_y)$, l'efecte del filtre es descriu matemàticament definint l'espectre filtrat com

$$
\mathcal{F}\{U_0\}_{\mathrm{filtrat}}(\nu_x,\nu_y):=H(\nu_x,\nu_y)\mathcal{F}\{U_0\}(\nu_x,\nu_y). \tag{16}
$$

La segona lent $L_2$ del sistema 4f recombina els components transmesos pel filtre i forma la imatge al pla $P_2$, situat al seu pla focal posterior. Per tant, llevat de factors constants, de fase i de la inversió geomètrica pròpia del sistema donada per l'Eq. (12), el camp reconstruït $U_2(x_2,y_2)$ és proporcional a la transformada de Fourier inversa de l'espectre filtrat,

$$
U_2(x_2,y_2)\propto \mathcal{F}^{-1}\left\{H(\nu_x,\nu_y)\mathcal{F}\{U_0\}(\nu_x,\nu_y)\right\}(x_2,y_2). \tag{17}
$$

En general, una funció de transferència òptica pot ser complexa i s'escriu com

$$
H(\nu_x,\nu_y)=|H(\nu_x,\nu_y)|e^{i\phi_H(\nu_x,\nu_y)}. \tag{18}
$$

Els filtres emprats en aquesta pràctica controlen principalment el mòdul de $H$, ja que transmeten, atenuen o bloquegen llum en regions concretes del pla de Fourier.

![Filtres espacials originals de l'informe](assets/figure_2_spatial_filters.png)

## Relacions experimentals emprades al muntatge

Les distàncies del muntatge han de satisfer, dins la incertesa experimental,

$$
P_0L_1\simeq f_1,\qquad L_1P_1\simeq f_1,\qquad P_1L_2\simeq f_2,\qquad L_2P_2\simeq f_2. \tag{19}
$$

Per tant,

$$
P_0P_2\simeq 2f_1+2f_2. \tag{20}
$$

L'augment transversal experimental es determina com

$$
|M|_{\mathrm{exp}}=\frac{h_2}{h_0}. \tag{21}
$$

Per a una xarxa periòdica de període $d$, els ordres de difracció satisfan

$$
d\sin\theta_m=m\lambda. \tag{22}
$$

La freqüència espacial corresponent és

$$
\nu_x=\frac{m}{d},\qquad m=0,\pm1,\pm2,\ldots \tag{23}
$$

i, mitjançant l'Eq. (8), la posició esperada de l'ordre $m$ al pla de Fourier és

$$
x_{1,m}\simeq \lambda f_1\frac{m}{d},\qquad m=0,\pm1,\pm2,\ldots \tag{24}
$$

Per a un filtre low-pass circular de radi efectiu $R$, la freqüència espacial de tall és

$$
\nu_c\simeq\frac{R}{\lambda f_1}. \tag{25}
$$

Per a una xarxa unidimensional, els ordres transmesos compleixen

$$
\left|\frac{m}{d}\right|\lesssim \nu_c, \tag{26}
$$

és a dir,

$$
|m|\lesssim \frac{dR}{\lambda f_1}. \tag{27}
$$

La resta del desenvolupament experimental - filtres high-pass, band-pass, direccionals i notch, i reconstrucció progressiva d'una xarxa rectangular mitjançant els seus harmònics - es conserva íntegrament al PDF original, que és el document canònic del projecte.
