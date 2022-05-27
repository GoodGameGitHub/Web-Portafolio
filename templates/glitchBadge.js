

/**
 * Settings
 **/

 const settings = {
	words: ['', 'Welcome', 'to','my','website','' ],
}



/**
 * Canvas
 **/

const $canvas = document.getElementById('canvas2')

const updateCanvasSize = () => {
  const { innerWidth, innerHeight, devicePixelRatio } = window
	
	const width      = 600
	const height     = 192 // innerHeight
	const pixelRatio = Math.min(devicePixelRatio, 2)
  
  $canvas.width  = width  * pixelRatio
  $canvas.height = height * pixelRatio
  
  $canvas.style.width  = width  + 'px'
  $canvas.style.height = height + 'px'
}

window.addEventListener('resize', updateCanvasSize)
updateCanvasSize()


/**
 * Context
 **/

const ctx2 = $canvas.getContext('2d')


/**
 * Glitch Effect
 **/

// Split Canvas
const $splitCanvas = document.createElement('canvas')
const splitCtx     = $splitCanvas.getContext('2d')

$splitCanvas.width  = $canvas.width
$splitCanvas.height = $canvas.height

// Draw Text
const drawText = (context, text, font, color) => {
  context.fillStyle    = 'green'
  context.font         = font
  context.textBaseline = 'middle'
  context.textAlign    = 'center'

  context.fillText(text, context.canvas.width / 2, context.canvas.height / 9 * 5)
}

// Offset
const offset = { x1: 0, y1:0, x2: 0, y2: 0 }

const randomOffset = (x, y) => {
	const randomX = Math.random() * (x + x) - x
	const randomY = Math.random() * (y + y) - y

  offset.x1 = randomX / 1
  offset.x2 = randomX / 2

  offset.y1 = randomY / 2
  offset.y2 = randomY / 4
}

// Glitch
const glitch = (context) => {
  for (let i = 0; i < randomInt(1, 10); i++) {
    const x = Math.random() * context.canvas.width
    const y = Math.random() * context.canvas.height

    const spliceWidth  = context.canvas.width - x
    const spliceHeight = randomInt(5, context.canvas.height / 3)

    context.drawImage(context.canvas, 0, y, spliceWidth, spliceHeight, x, y, spliceWidth, spliceHeight)
    context.drawImage(context.canvas, spliceWidth, y, x, spliceHeight, 0, y, x, spliceHeight)
  }
}

// Blur
const blur = (context, splitContext) => {
  splitContext.clearRect(0, 0, splitContext.canvas.width, splitContext.canvas.height)

  splitContext.drawImage(context.canvas, 0, 0)

  context.globalAlpha = .5

  context.drawImage(splitContext.canvas, offset.x1, offset.y1)
  context.drawImage(splitContext.canvas, offset.x1, offset.y1)

  context.drawImage(splitContext.canvas, offset.x2, offset.y2)
  context.drawImage(splitContext.canvas, offset.x2, offset.y2)

  context.globalAlpha = 1
}

// Split
const split = (context, splitContext) => {
  splitContext.clearRect(0, 0, splitContext.canvas.width, splitContext.canvas.height)

  let w = context.canvas.width
  let h = context.canvas.height

  let x = Math.random() * w
  let y = Math.random() * h

  let spliceWidth = w - x;
  let spliceHeight = randomInt(5, h / 3)

  splitContext.drawImage(context.canvas, 0, 0)

  splitContext.globalCompositeOperation = 'source-in'

  splitContext.fillStyle = 'green'

  splitContext.fillRect(0, 0, context.canvas.width / randomInt(2, 10), context.canvas.height / 1)

  context.drawImage(splitContext.canvas, 0, 0, spliceWidth, spliceHeight, x, y, spliceWidth, spliceHeight)


  splitContext.globalCompositeOperation = 'source-over'
}

// ...
let change = false
let wi = 0

const nextWord = () => {
  change = true

  setTimeout(() => {
    change = false
  }, 280)

  setTimeout(() => {
    if (wi < settings.words.length - 1) {
      wi++
    } else {
      wi = 0
    }
  }, 140)
}


/**
 * Loop
 **/

requestAnimationFrame(function tick(timestamp) {
  const { width, height } = $canvas
	const pixelRatio = Math.min(window.devicePixelRatio, 2)
  
  ctx2.clearRect(0, 0, width, height)
  
  // background
  ctx2.fillStyle = '#111' // '#099268'
  ctx2.fillRect(0, 0, width, height)
	
	// ...
	// drawText(ctx2, 'Hello', `800 128px Monospace`, '#eee')
	
	drawText(ctx2, settings.words[wi], `800 ${ 128 * pixelRatio }px 'Courier Prime', Monospace`, '#eee')
	

  if (change) {
    glitch(ctx2)

    randomOffset(12, 2)
    blur(ctx2, splitCtx)

    split(ctx2, splitCtx)
  }
	
	
  requestAnimationFrame(tick)
})

setInterval(nextWord, 2000)



/**
 * Utils
 **/

function randomInt(min, max) {
  return Math.round( min - 0.5 + Math.random() * (max - min + 1))
}