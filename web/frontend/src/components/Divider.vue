<template>
  <v-row>
    <v-col cols="12" sm="6" offset-sm="3">
      <v-card>
        <v-list two-line>
          <template v-for="(item, index) in items.slice(0, 6)">
            <v-subheader v-if="item.header" :key="item.header">{{ item.header }}</v-subheader>
            <v-divider v-else-if="item.divider" :key="index" :inset="item.inset"></v-divider>
            <v-list-item v-else :key="item.title">
              <v-list-item-avatar>
                <img :src="item.avatar" />
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-html="item.title"></v-list-item-title>
                <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </v-card>
    </v-col>
  </v-row>
</template>
<style>
.v-list-item__title {
  align-self: center;
  font-size: 1.3rem;
  /* display: inline-block; */
  position: absolute;
  width: 30%;
  top: 10px;
}
.v-list-item__subtitle {
  /* display: inline-block; */
  margin-top: 10px;
  position: absolute;
  width: 20%;
}
</style>
<script>
export default {
  data: () => ({
    items: [
      { header: "식품목록" },
      {
        avatar:
          "https://ifh.cc/g/eXT5Yy.jpg",
        title: "파프리카",
        subtitle: "D-5"
      },
      { divider: true, inset: true },
      {
        avatar:
          "https://ifh.cc/g/RRUTKG.jpg",
        title: "토마토",
        subtitle: "D-3"
      },
      { divider: true, inset: true },
      {
        avatar:
          "https://ifh.cc/g/tqTZGN.jpg",
        title: "계란",
        subtitle: "D-12"
      }
    ]
  })
};
</script>