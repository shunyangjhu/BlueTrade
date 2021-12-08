<template>
  <div class="s-canvas">
    <canvas id="s-canvas" :width="picWidth" :height="picHeight"></canvas>
  </div>
</template>
<script>
export default {
  name: 'Validate',
  data(){
    return {
      bgColorMin: 180,
      bgColorMax: 230,
      picHeight: 38,
      picWidth: 120
    }
  },
  props: {
    validateCode: {
      type: String,
      default: "1234"
    },
  },
  methods: {
    randomColor(min, max) {
      const r = Math.floor(Math.random() * (max - min) + min);
      const g = Math.floor(Math.random() * (max - min) + min);
      const b = Math.floor(Math.random() * (max - min) + min);
      return 'rgb(' + r + ',' + g + ',' + b + ')'
    },
    drawValidateCode() {
      const canvas = document.getElementById('s-canvas');
      const cs = canvas.getContext('2d');
      cs.textBaseline = 'bottom';
      cs.fillStyle = this.randomColor(this.bgColorMin, this.bgColorMax);
      cs.fillRect(0, 0, this.picWidth, this.picHeight);

      for (let i = 0; i < 4; i++) {
        this.drawNumber(cs, this.validateCode[i], i);
      }

      this.drawLine(cs);
      this.drawDot(cs);
    },
    drawNumber(ctx, number, i) {
      ctx.fillStyle = this.randomColor(0, 150)
      ctx.font = Math.floor(Math.random() * (38 - 18) + 18) + 'px Times New Roman';
      const x = (i + 1) * (this.picWidth / 5);
      const y =  Math.floor(Math.random() * (38 - 35) + 38);
      const deg =  Math.floor(Math.random() * (30 + 30) - 30);

      ctx.translate(x, y);
      ctx.rotate(deg * Math.PI / 180);
      ctx.fillText(number, 0, 0);
      ctx.rotate(-deg * Math.PI / 180);
      ctx.translate(-x, -y);
    },
    drawLine(ctx) {
      for (let i = 0; i < 5; i++) {
        ctx.strokeStyle = this.randomColor(50, 200);
        ctx.beginPath()
        ctx.moveTo(Math.floor(Math.random() * this.picWidth), Math.floor(Math.random() * this.picHeight));
        ctx.lineTo(Math.floor(Math.random() * this.picWidth), Math.floor(Math.random() * this.picHeight));
        ctx.stroke();
      }
    },
    drawDot(ctx) {
      for (let i = 0; i < 30; i++) {
        ctx.fillStyle = this.randomColor(0, 255);
        ctx.beginPath();
        ctx.arc(Math.floor(Math.random() * this.picWidth), Math.floor(Math.random() * this.picHeight),1,0,2 * Math.PI);
        ctx.fill();
      }
    }
  },
  watch: {
    validateCode() {
      this.drawValidateCode();
    }
  },
  mounted() {
    this.drawValidateCode();
  }
}
</script>

<style scoped>
</style>
