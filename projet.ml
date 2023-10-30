load "graphics.cma";;
open Graphics;;
open Complex;;

(* dimensions de base *)
open_graph " 600x600";;

let lvl_of point c = (* a et b sont tels que Z_(p,c)(0)= a+i.b = point *)
        (*let a = point.re and b = point.im in  coordonnées du point p *)
        (*let cr = c.re and ci = c.im in *)
        let xJulia = ref (point.re) in
        let yJulia = ref (point.im) in
        let xSuivant= ref 0. in
        let ySuivant= ref 0. in
        let borne = 256 in
        let k = ref 0 in
        while (( (!xJulia)*.(!xJulia) +. (!yJulia)*.(!yJulia) < 4. )&&( (!k)<borne )) do
                xSuivant:= (!xJulia)*.(!xJulia) -. (!yJulia)*.(!yJulia) +. (c.re);
                ySuivant:= 2.*.(!xJulia)*.(!yJulia) +. (c.im);
                (* on actualise les valeurs *)
                xJulia:= !xSuivant;
                yJulia:= !ySuivant;
                (* on incrémente la sortie n, l'indice du coloriage *)
                k:= !k+1;
        done;
        (!k);;
(* (* FONCTION RECURSIVE *)
let lvl_of_recursive point c =
        let xJulia = point.re in
        let yJulia = point.im in
        let xSuivant= 0. in
        let ySuivant= 0. in
        let borne = 256 in
        let k = 0 in
        let rec aux x y n1 = match x,y,n1 with
                |(x,y,n) when (( (x)*.(x) +. (y)*.(y) < 4. )&&( n<borne ))
                        ->      xSuivant = (x)*.(x) -. (y)*.(y) +. (c.re);
                                ySuivant = 2.*.(x)*.(y) +. (c.im);
                                (* on actualise les valeurs *)
                                x = xSuivant;
                                y = ySuivant;
                                (* on incrémente la sortie n, l'indice du coloriage *)
                                n = n+1; aux x y n (* c'est une boucle while *)
                | _ -> n1;
                in aux xJulia yJulia k;;
*)

let julia c zoom = (* constante c [Complex] et coefficient de zoom [float] *)
        let k = ref 0 in
        (* on définit ici l'intervlle de représentation des courbes de Julia *)
        for x=(-300) to (300) do
                for y=(-300) to (300) do
                        let point = {re = (float_of_int x) /. zoom ; im = (float_of_int y) /. zoom} in
                        k:=((lvl_of point c)*10);
                        set_color (rgb ((!k)*15) ((!k)*15) ((!k))*15);
                        (* le point central intervient ici *)
                        plot (x+300) (y+300);
                done;
        done;;
(*
(* FONCTION RECURSIVE *)
let julia_rec c zoom plageCapture =
        let k = ref 0 in
        let rec parcoursX plage = match plage with
        | []->()
        | t::q -> let rec parcoursY l = match l with
                        | [] -> ()
                        | d::f -> let point = {re = (float_of_int t) /. zoom ; im = (float_of_int d) /. zoom} in
                                                        (* coordonnée (t,d) pour le coloriage*)
                                                        k:=((lvl_of point c)*10);
                                                        set_color (rgb ((!k)*15) ((!k)*15) ((!k))*15);
                                                        (* le point central intervient ici *)
                                                        plot (t+300) (d+300);
                                                        parcoursY f;
                                 in parcoursY q; (* on colore les pixels dessous*)
        in parcoursX plageCapture;; (* on colore les colonnes suivantes *)
*)

(* APPLICATION *)
let c = {re = -0.76; im = 0.12} in
julia c 150.;;


