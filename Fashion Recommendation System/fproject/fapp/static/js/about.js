// Example: Adding a class on hover to change the background color
document.querySelectorAll('.person-card').forEach(card => {
    card.addEventListener('mouseover', () => {
        card.classList.add('hovered');
    });
    card.addEventListener('mouseout', () => {
        card.classList.remove('hovered');
    });
});
gsap.from('img',{
    scale:0,
    stagger:.3,
    duration:1.3,
    x:-200,
    // yoyo:true,
    // repeat:-1,
})
gsap.from('h2,h4,p',{
    y:100,
    duration:0.6,
    stagger:.2,
    scale:0
})
