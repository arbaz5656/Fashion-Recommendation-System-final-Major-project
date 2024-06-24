gsap.from('.navbar h1, .navbar button',{
    y:-100,
    opacity:0,
    stagger:.2,
})
gsap.from('.navbar-right',{
    y:-100,
    opacity:0,
    stagger:.2,
})
gsap.from('.category',{
    y:-100,
    opacity:0,
    stagger:.2,
    delay:.5,
})
gsap.from('.card',{
    scale:0,
    y:300,
    delay:1,
    
    // repeat:-1,
    stagger:.4,
   
})
gsap.from('.item-container  .item-card',{
    opacity:0,
    stagger:.2,
    x:-100,
    delay:3,   
})
gsap.from('.sub-category',{
    opacity:0,
    y:-100,
    delay:3,
})