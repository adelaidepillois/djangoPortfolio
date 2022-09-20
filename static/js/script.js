

//GESTION ONGLET + AFFICHAGE CONTENU
const onglets = document.querySelectorAll('.onglets');
const contenu = document.querySelectorAll('.contenu')
let index = 0;

onglets.forEach(onglet => {
    onglet.addEventListener('click', () => {
        if (onglet.classList.contains('active')) {
            return;
        } else {
            document.getElementById('onglets').classList.add('active');
            onglet.classList.add('active');
        }
        index = onglet.getAttribute('data-anim');
        console.log(index);

        for (i = 0; i < onglets.length; i++) {
            if (onglets[i].getAttribute('data-anim') != index) {

                onglets[i].classList.remove('active');
            }
        }
        for (j = 0; j < contenu.length; j++) {
            if (contenu[j].getAttribute('data-anim') == index) {

                contenu[j].classList.add('activeContenu');
            } else {
                contenu[j].classList.remove('activeContenu');

            }
        }
    })
})


//FLIP CARD
var cards = document.querySelectorAll('.card');

[...cards].forEach((card)=>{
  card.addEventListener( 'click', function() {
    card.classList.toggle('is-flipped');
  });
});



var curseur = document.getElementById('cursor1');
var centreYcurseur = parseInt(getComputedStyle(curseur, null).height) / 2;
var centreXcurseur = parseInt(getComputedStyle(curseur, null).width) / 2;

window.addEventListener('mousemove', e => {
    delay: 8,
    curseur.style.left = e.pageX - centreXcurseur + "px"
    curseur.style.top = e.pageY - centreYcurseur + "px"

})


/**
 * Calcul la position de l'élément par rapport au haut de la page
 * @param {HTMLElement} element
 * @return {number}
 */
function offsetTop(element, acc = 0) {
    if (element.offsetParent) {
        return offsetTop(element.offsetParent, acc + element.offsetTop);
    }
    return acc + element.offsetTop;

}


//PARALLAX
/**
 * @property {HTMLElement}element
 * @property {{y: number, r:number, variable: boolean}} options
 */
class Parallax {
    /**
     *
     * @param {HTMLElement} element
     */
    constructor(element) {
        this.element = element;
        this.options = this.parseAttribute();

        this.onScroll = this.onScroll.bind(this);
        this.onIntersection = this.onIntersection.bind(this);
        this.onResize = this.onResize.bind(this);


        this.elementY = offsetTop(this.element) + this.element.offsetHeight / 2;
        const observer = new IntersectionObserver(this.onIntersection);
        observer.observe(element);
        this.onScroll();
    }

    parseAttribute() {
        const defaultOptions = {
            y: 0.2,
            r: 0,
            variable: false,
        }
        if (this.element.dataset.parallax.startsWith('{')) {
            return {...defaultOptions, ...JSON.parse(this.element.dataset.parallax)}
        }
        return {...defaultOptions, y: parseFloat(this.element.dataset.parallax)}
    }

    /**
     *
     * @param {IntersectionObserverEntry[]} entries
     */
    onIntersection(entries) {
        for (const entry of entries) {
            if (entry.isIntersecting) {
                document.addEventListener("scroll", this.onScroll);
                window.addEventListener("resize", this.onResize);
                this.elementY = offsetTop(this.element) + this.element.offsetHeight / 2;
            } else {
                document.removeEventListener("scroll", this.onScroll);
                window.removeEventListener('resize', this.onResize);
            }
        }
    }

    onResize() {
        this.elementY = offsetTop(this.element) + this.element.offsetHeight / 2;
        this.onScroll()
    }

    onScroll() {
        window.requestAnimationFrame(() => {
            const screenY = window.scrollY + window.innerHeight / 2;
            const diffY = this.elementY - screenY;
            const translateY = diffY * -1 * this.options.y;
            var scrollPos = $(this).scrollTop();
            if (this.options.variable) {
                this.element.style.setProperty(
                    "--parallaxY",
                    `translateY(${translateY}px)`
                );
                $(".bg-landing").css({
                    'background-size': 100 - scrollPos + '%'
                });
            } else {
                let transform = `translateY(${translateY}px)`
                if (this.options.r) {
                    transform += `rotate(${diffY * this.options.r}deg)`
                }
                // When the user scrolls down 50px from the top of the document, resize the moon
                if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
                    if ($(window).height() >= 650) {
                        document.getElementById("smpoint").style.top = "30%";
                        document.getElementById("smpoint").style.width = "160px";
                        document.getElementById("smpoint").style.right = "3%";
                        document.getElementById("smpoint").style.height = "160px";

                        /*                        document.getElementById("moon").style.top = "70%";
                                                document.getElementById("moon").style.width = "200px";
                                                document.getElementById("moon").style.left = "70%";
                                                document.getElementById("moon").style.height = "200px";*/
                    }

                } else {
                    if ($(window).height() >= 650) {
                        document.getElementById("smpoint").style.top = "15%";
                        document.getElementById("smpoint").style.width = "60px";
                        document.getElementById("smpoint").style.right = "3%";
                        document.getElementById("smpoint").style.height = "60px";
                        document.getElementById("mdpoint").style.top = "-11%";
                        document.getElementById("mdpoint").style.right = "42%";
                        document.getElementById("lgpoint").style.top = "100%";
                        document.getElementById("lgpoint").style.right = "50%";


                        /*                        document.getElementById("moon").style.width = "300px";
                                                document.getElementById("moon").style.left = "-30px";
                                                document.getElementById("moon").style.height = "300px";
                                                document.getElementById("moon").style.top = "100px";*/
                    }

                }
                this.element.style.setProperty(
                    "transform",
                    transform
                );
            }
        })
    }

    /**
     *
     * @returns {Parallax[]}
     */
    static bind() {
        return Array.from(document.querySelectorAll('[data-parallax]')).map(
            (element) => {
                return new Parallax(element);
            }
        );
    }
}

Parallax.bind();

