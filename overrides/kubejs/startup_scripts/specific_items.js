StartupEvents.registry('item', event => {
    event.create('pumpkinite_ingot')
    .tag('forge:ingots')
    event.create('cheesite_wedge').food(food => {
        food
        .hunger(6)
        .saturation(1.2)
    })
})
