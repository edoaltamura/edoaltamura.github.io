+++
title = "MACSIS"
+++
___
### Substructures in galaxy clusters | Master thesis
##### _Observability study using the MACSIS hydrodynamical simulation and Sunyaev-Zel’dovich signals_

___
#### What is **MACSIS**?
MACSIS stands for *MAssive ClusterS and Intercluster Structures*. It is a project consisting in the simulation of a collection of extraordinarily large galaxy clusters. The total mass of these clusters varies between 10<sup>15</sup> M<sub>&odot;</sub> and 10<sup>16</sup> M<sub>&odot;</sub>, making them an incredibly good representation of the **most massive**, **rarest** and **youngest** astrophysical objects that we would ever observe in our Universe.

The MACSIS project originated from the hard work of Barnes *et al.* ([2015](https://ui.adsabs.harvard.edu/abs/2015eheu.conf...41B), [2017](https://ui.adsabs.harvard.edu/abs/2017MNRAS.465..213B)), who used the [```Gadget-3```](https://ui.adsabs.harvard.edu/abs/2005MNRAS.364.1105S) code to simulate a gigantic 3.2 Gpc-wide region of the Universe, large enough to exploit the chances of finding the rare and large galaxy clusters.

#### Some "*back-of-the-napkin*" notes on MACSIS clusters
Before diving into the particular MACSIS clusters, let us explain how a galaxy clusters form in the Universe - and in particular how can they grow so much. Of course, if you have some knowledge of structure formation in late-time Cosmology, then you may skip this paragraphs.

The process that governs the origin and evolution of very large gravitational systems is called **hierarchical structure formation**. The matter density perturbations, imprinted since the end of inflation, can survive the expansion of the Universe. At early times they are still very small (∼ 0.001% compared to the background density) and grow linearly with time. At late times though, they outgrow the background density field by more than ≈ 200 times and they become non-linear. This process of *gravitational collapse* applies to every region of the Universe that happens to be overdense, but we have implicitly assumed that each of those regions is independent of the others, i.e. no interaction exists between neighbouring overdense regions. This model alone is clearly quite unrealistic: it implies that gravity would *only* affect all the matter inside the overdense region, while leaving everything outside unchanged and unaffected. We though know that gravity acts on very large scales too - it has an *infinite* force range - and therefore different neighbouring overdense regions must indeed interact gravitationally.

These overdense regions are the ancestors of galaxy clusters. The gravitational pull among them causes these objects to fall into each other and merge down into a larger galaxy cluster. This process happens at all scales and is said to reflect a bottom-up scenario: small structures start merging and form large structures at later on in cosmic history. This clearly means that there exists a **hierarchy** of structures: as the Universe evolves, larger and larger structures may arise from the interaction of smaller ones, as one can see from the simulation in the video below.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/OmX_4p1QxkU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

##### Why the **most massive** clusters?
The 3.2 Gpc box simulated in the first stage of the MACSIS project includes galaxy clusters (or more precisely, dark matter halos) with all masses: from the ∼10<sup>16</sup> M<sub>&odot;</sub> quoted above, down to 10<sup>12-13</sup> M<sub>&odot;</sub>, limited by the mass resolution limit. The first stage, however, aims at covering a very large volume, at the expenses of the resolution with which the matter field is simulated. Think of this process as a quick survey of the cosmological volume, run for identifying where the collapsed structures are located. The second stage, instead, consists in re-running the simulation of *some* of these structures with much higher resolution: this is known as *zoom simulation* technique. The sub-sample of galaxy clusters to be re-simulated is **defined by the needs and the aim of the project**. In this case, the interest was towards extremely large clusters, so the zoom simulations involved the top 90 largest clusters, followed by 300 runner-ups selected randomly between 10<sup>15.0</sup> M<sub>&odot;</sub> and 10<sup>15.6</sup> M<sub>&odot;</sub>.
##### Why the **rarest**?
According to the hierarchical structure formation, the Universe was mostly populated with low-mass halos at very early times


![mass_function_z_0](/projects_repo/mass_function.png)

##### Why the **youngest**?

<div style="text-align:center"> 
  <button onclick="playPause()" style="border-radius: 5px; color: black; background-color: #FFFFC0;">Play/Pause</button> 
  <button onclick="makeBig()" style="border-radius: 5px; color: black; background-color: #FFFFC0;">Big</button>
  <button onclick="makeSmall()" style="border-radius: 5px; color: black; background-color: #FFFFC0;">Small</button>
  <button onclick="makeNormal()" style="border-radius: 5px; color: black; background-color: #FFFFC0;">Normal</button>
  <br><br>
  <video id="video1" width="700">
    <source src="/projects_repo/mass_function_vid.mp4" type="video/mp4">
  </video>
</div> 

<script> 
var myVideo = document.getElementById("video1"); 

function playPause() { 
  if (myVideo.paused) 
    myVideo.play(); 
  else 
    myVideo.pause(); 
} 

function makeBig() { 
    myVideo.width = 1000; 
} 

function makeSmall() { 
    myVideo.width = 400; 
} 

function makeNormal() { 
    myVideo.width = 700; 
} 
</script> 


___
|  |  |  |
| --- | --- | --- |
| Master_Thesis S7 | <a href="/projects_repo/Master_Thesis_S7.pdf">```pdf```</a> | ```github``` |
| Master_Thesis S8 | <a href="/projects_repo/Master_Thesis_S8.pdf">```pdf```</a> | ```github``` |

___
[**International Conference of Physics Students**](https://icps.cologne/) | 8.2019\\
Cologne, Germany

|  |  |  |
| --- | --- | --- |
| Conference poster | ```pdf``` | ```github``` |
| Talk presentation | ```pdf``` | ```github``` |

___
